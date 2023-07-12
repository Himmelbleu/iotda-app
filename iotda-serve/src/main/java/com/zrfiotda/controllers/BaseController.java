package com.zrfiotda.controllers;

import com.zrfiotda.pojos.*;
import com.zrfiotda.service.BaseService;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@CrossOrigin
public class BaseController {

    private final BaseService service;

    public BaseController(BaseService service) {
        this.service = service;
    }


    /**
     * pageNum：页码
     * pageSize：一页数量
     */
    @PostMapping("/select/all/cover")
    public PageCover selectCoverAll(@RequestBody Map<String, Object> map) {
        return service.selectCoverAll(map);
    }

    /**
     * pageNum：页码
     * pageSize：一页数量
     */
    @PostMapping("/select/all/smoke")
    public PageSmoke selectSmokeAll(@RequestBody Map<String, Object> map) {
        return service.selectSmokeAll(map);
    }

    @PostMapping("/get/smoke/count")
    public SmokeCount getSmokeCount() {
        return service.getSmokeCount();
    }

    @PostMapping("/get/cover/count")
    public CoverCount getCoverCount() {
        return service.getCoverCount();
    }

    @PostMapping("/get/recent/coverAndSmoke")
    public CoverAndSmoke getRecentCoverAndSmoke() {
        return service.getRecentCoverAndSmoke();
    }

}
