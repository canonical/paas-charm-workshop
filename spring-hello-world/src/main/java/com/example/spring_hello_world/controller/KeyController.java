package com.example.spring_hello_world.controller;

import com.example.spring_hello_world.model.SecretKey;
import com.example.spring_hello_world.service.KeyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
public class KeyController {
    @Autowired
    private KeyService keyService;

    @GetMapping("/health")
    public ResponseEntity<String> healthCheck() {
        return ResponseEntity.ok("{\"status\": \"ok\"}");
    }

    @GetMapping("/fibonacci/{n}")
    public ResponseEntity<List<Integer>> getFibonacci(@PathVariable int n) {
        List<Integer> result = keyService.fibonacci(n);
        return ResponseEntity.ok(result);
    }

    @PostMapping("/keys")
    public ResponseEntity<SecretKey> createKey(@RequestBody SecretKey key) {
        SecretKey createdKey = keyService.createKey(key);
        return ResponseEntity.status(201).body(createdKey);
    }

    @GetMapping("/keys/{id}")
    public ResponseEntity<SecretKey> getKey(@PathVariable UUID id) {
        Optional<SecretKey> key = keyService.getKey(id);
        return key.map(ResponseEntity::ok)
                  .orElseGet(() -> ResponseEntity.notFound().build());
    }
}