package com.web93.travel.service;

import com.web93.travel.data.RegisterData;
import com.web93.travel.entity.User;
import com.web93.travel.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.DigestUtils;

import java.util.UUID;

@Service
public class UserService {

    @Autowired
    private UserMapper userMapper;

    public boolean register(RegisterData data){
        String salt = UUID.randomUUID().toString();
        User user = new User();
        user.setUserName(data.getUserName());
        user.setPassword(DigestUtils.md5DigestAsHex((data.getPassword() + salt).getBytes()));
        user.setSalt(salt);
        return 1 == userMapper.insert(user);
    }
}
