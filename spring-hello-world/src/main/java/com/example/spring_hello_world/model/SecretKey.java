package com.example.spring_hello_world.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Table;
import jakarta.persistence.Column;
import java.util.UUID;

@Entity
@Table(name = "secret_keys")
public class SecretKey {
    @Id
    private UUID id; // UUID type for the id

    @Column(nullable = false)
    private String value;

    // Constructor
    public SecretKey() {
        this.id = UUID.randomUUID(); // Generate a new UUID when the object is created
    }

    // Getters and Setters
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
}
