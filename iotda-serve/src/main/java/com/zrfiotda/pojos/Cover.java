package com.zrfiotda.pojos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Cover {

    private int id;
    private String temp;
    private String accelX;
    private String accelY;
    private String accelZ;
    private String coverStatus;
    private String date;
    private String sno;
    private String name;

}
