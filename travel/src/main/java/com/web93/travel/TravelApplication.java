package com.web93.travel;

import tk.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@MapperScan("com.web93.travel.mapper")
@SpringBootApplication
public class TravelApplication {

    public static void main(String[] args) {
        SpringApplication.run(TravelApplication.class, args);
    }

}