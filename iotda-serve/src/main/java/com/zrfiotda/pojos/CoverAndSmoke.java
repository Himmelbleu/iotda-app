package com.zrfiotda.pojos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CoverAndSmoke {

    private List<String> covers;
    private List<String> smokes;
    private List<String> dates;

}
