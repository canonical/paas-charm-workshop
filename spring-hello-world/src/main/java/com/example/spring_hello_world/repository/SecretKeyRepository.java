package com.example.spring_hello_world.repository;

import com.example.spring_hello_world.model.SecretKey;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SecretKeyRepository extends JpaRepository<SecretKey, Long> {
}