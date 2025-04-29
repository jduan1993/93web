package com.web93.travel.data;

import javax.validation.constraints.NotBlank;
import org.hibernate.validator.constraints.Length;

public class RegisterData {

    @NotBlank(message = "用户名不能为空")
    private String userName;

    @Length(min = 8, max = 20, message = "密码必须为8至20位")
    private String password;

    public String getUserName() {
        return userName;
    }

    public String getPassword() {
        return password;
    }
}
