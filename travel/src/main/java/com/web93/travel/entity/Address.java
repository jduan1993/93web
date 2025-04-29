package com.web93.travel.entity;

import javax.persistence.*;

@Table(name = "address_info")
public class Address {
    @Id
    private Integer id;

    @Column(name = "site_name")
    private String siteName;

    private String province;

    private String city;

    private String district;

    private String address;

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
}