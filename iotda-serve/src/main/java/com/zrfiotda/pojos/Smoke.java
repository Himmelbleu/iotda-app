package com.zrfiotda.pojos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Smoke {

    private int id;
    private String smokeValue;
    private String beepStatus;
    private String date;
    private String sno;
    private String name;

}
