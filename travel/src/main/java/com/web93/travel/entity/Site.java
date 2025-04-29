package com.web93.travel.entity;

import javax.persistence.*;

@Table(name = "site_info")
public class Site {
    @Id
    private Integer id;

    private String province;

    private String city;

    private String district;

    @Column(name = "site_name")
    private String siteName;

    private String address;

    @Column(name = "open_time")
    private String openTime;

    private String grade;

    /**
     * @return id
     */
    public Integer getId() {
        return id;
    }

    /**
     * @param id
     */
    public void setId(Integer id) {
        this.id = id;
    }

    /**
     * @return province
     */
    public String getProvince() {
        return province;
    }

    /**
     * @param province
     */
    public void setProvince(String province) {
        this.province = province == null ? null : province.trim();
    }

    /**
     * @return city
     */
    public String getCity() {
        return city;
    }

    /**
     * @param city
     */
    public void setCity(String city) {
        this.city = city == null ? null : city.trim();
    }

    /**
     * @return district
     */
    public String getDistrict() {
        return district;
    }

    /**
     * @param district
     */
    public void setDistrict(String district) {
        this.district = district == null ? null : district.trim();
    }

    /**
     * @return site_name
     */
    public String getSiteName() {
        return siteName;
    }

    /**
     * @param siteName
     */
    public void setSiteName(String siteName) {
        this.siteName = siteName == null ? null : siteName.trim();
    }

    /**
     * @return address
     */
    public String getAddress() {
        return address;
    }

    /**
     * @param address
     */
    public void setAddress(String address) {
        this.address = address == null ? null : address.trim();
    }

    /**
     * @return open_time
     */
    public String getOpenTime() {
        return openTime;
    }

    /**
     * @param openTime
     */
    public void setOpenTime(String openTime) {
        this.openTime = openTime == null ? null : openTime.trim();
    }

    /**
     * @return grade
     */
    public String getGrade() {
        return grade;
    }

    /**
     * @param grade
     */
    public void setGrade(String grade) {
        this.grade = grade == null ? null : grade.trim();
    }
}