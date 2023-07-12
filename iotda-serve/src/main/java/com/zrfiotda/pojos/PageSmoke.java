package com.zrfiotda.pojos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PageSmoke {

    private int pageSize;
    private long total;
    private List<Smoke> list;

}
