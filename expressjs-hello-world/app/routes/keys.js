const express = require('express');
const { Pool } = require('pg');
const { v4: uuidv4 } = require('uuid');

const router = express.Router();

// PostgreSQL database connection
const pool = new Pool({
    connectionString: process.env.POSTGRESQL_DB_CONNECT_STRING,
});

// Create key endpoint
router.post('/', async (req, res) => {
    const key = req.body;

    if (!key || !key.value) {
        return res.status(400).json({ error: "Value is required" });
    }

    const keyID = uuidv4();

    try {
        await pool.query("INSERT INTO secret_keys (id, value) VALUES ($1, $2)", [keyID, key.value]);
        res.status(201).json({ key_id: keyID });
    } catch (err) {
        console.error("Error creating key:", err);
        res.status(500).json({ error: "Error creating key" });
    }
});

// Get key endpoint
router.get('/:keyID', async (req, res) => {
    const keyID = req.params.keyID;

    try {
        const result = await pool.query("SELECT value FROM secret_keys WHERE id = $1", [keyID]);

        if (result.rows.length === 0) {
            return res.status(404).json({ error: "Key not found" });
        }

        res.json({ key_id: keyID, value: result.rows[0].value });
    } catch (err) {
        console.error("Error retrieving key:", err);
        res.status(500).json({ error: "Error retrieving key" });
    }
});

module.exports = router;