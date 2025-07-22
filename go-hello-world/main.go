package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/google/uuid"
	_ "github.com/lib/pq"
)

var db *sql.DB

type SecretKey struct {
	Value string `json:"value"`
}

// Initialize the database connection
func init() {
	var err error
	dsn := os.Getenv("POSTGRESQL_DB_CONNECT_STRING")
	if strings.Contains(dsn, "?") {
		dsn += "&sslmode=disable" // Change to "require" if you want SSL
	} else {
		dsn += "?sslmode=disable" // Change to "require" if you want SSL
	}
	fmt.Println("DSN: ", dsn)
	db, err = sql.Open("postgres", dsn)
	if err != nil {
		log.Fatal(err)
	}
}

// Health check endpoint
func healthCheck(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}

// Fibonacci endpoint
func fibonacci(n int) ([]int, error) {
	if n < 0 {
		return nil, fmt.Errorf("Invalid input")
	}
	fibSequence := make([]int, n)
	a, b := 0, 1
	for i := 0; i < n; i++ {
		fibSequence[i] = a
		a, b = b, a+b
	}
	return fibSequence, nil
}

func getFibonacci(w http.ResponseWriter, r *http.Request) {
	nStr := r.URL.Path[len("/fibonacci/"):]

	n, err := strconv.Atoi(nStr)
	if err != nil || n < 0 {
		http.Error(w, `{"error": "Invalid input"}`, http.StatusBadRequest)
		return
	}

	result, err := fibonacci(n)
	if err != nil {
		http.Error(w, `{"error": "Invalid input"}`, http.StatusBadRequest)
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{"fibonacci": result})
}

// Create key endpoint
func createKey(w http.ResponseWriter, r *http.Request) {
	var key SecretKey
	if err := json.NewDecoder(r.Body).Decode(&key); err != nil {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	if key.Value == "" {
		http.Error(w, "Value is required", http.StatusBadRequest)
		return
	}

	var keyID uuid.UUID = uuid.New()
	_, err := db.Exec("INSERT INTO secret_keys (id, value) VALUES ($1, $2)", keyID, key.Value)
	if err != nil {
		http.Error(w, fmt.Sprintf("Error creating key: %s", err.Error()), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(map[string]string{"key_id": keyID.String()})
}

// Get key endpoint
func getKey(w http.ResponseWriter, r *http.Request) {
	keyID := r.URL.Path[len("/keys/"):]

	var id uuid.UUID
	if err := id.UnmarshalText([]byte(keyID)); err != nil {
		http.Error(w, "Invalid key ID", http.StatusBadRequest)
		return
	}

	var value string
	err := db.QueryRow("SELECT value FROM secret_keys WHERE id = $1", id).Scan(&value)
	if err == sql.ErrNoRows {
		http.Error(w, "Key not found", http.StatusNotFound)
		return
	} else if err != nil {
		http.Error(w, "Error retrieving key", http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(map[string]interface{}{"key_id": keyID, "value": value})
}

func main() {
	http.HandleFunc("/health", healthCheck)      // Health check endpoint
	http.HandleFunc("/fibonacci/", getFibonacci) // Fibonacci endpoint
	http.HandleFunc("/keys", createKey)          // Create key endpoint
	http.HandleFunc("/keys/", getKey)            // Get key endpoint

	port := ":8080"
	log.Fatal(http.ListenAndServe(port, nil))
}
