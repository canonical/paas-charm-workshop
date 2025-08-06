package com.example.spring_hello_world;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;

@SpringBootApplication()
public class SpringHelloWorldApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringHelloWorldApplication.class, args);
	}

}
