package com.example.spring_hello_world.service;

import com.example.spring_hello_world.model.SecretKey;
import com.example.spring_hello_world.repository.SecretKeyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
import java.util.Optional;
import java.util.ArrayList;

@Service
public class KeyService {
    @Autowired
    private SecretKeyRepository secretKeyRepository;

    @Transactional
    public SecretKey createKey(SecretKey key) {
        return secretKeyRepository.save(key);
    }

    public Optional<SecretKey> getKey(Long id) {
        return secretKeyRepository.findById(id);
    }

    public List<Integer> fibonacci(int n) {
        if (n < 0) throw new IllegalArgumentException("Invalid input");
        List<Integer> fibSequence = new ArrayList<>();
        int a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            fibSequence.add(a);
            int next = a + b;
            a = b;
            b = next;
        }
        return fibSequence;
    }
}
