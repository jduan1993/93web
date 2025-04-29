package com.web93.travel.controller;

import com.web93.travel.data.RegisterData;
import com.web93.travel.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/register")
    public String register(@Valid RegisterData data) {
        boolean result = userService.register(data);
        if (result) {
            return "注册成功！";
        }
        return "注册失败！";
    }
}
