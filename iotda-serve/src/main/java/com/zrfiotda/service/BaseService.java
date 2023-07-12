package com.zrfiotda.service;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import com.zrfiotda.mappers.BaseMapper;
import com.zrfiotda.pojos.*;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class BaseService {

    private final BaseMapper mapper;

    public BaseService(BaseMapper mapper) {
        this.mapper = mapper;
    }

    public PageCover selectCoverAll(Map<String, Object> map) {
        Page<?> page = PageHelper.startPage((Integer) map.get("pageNum"), (Integer) map.get("pageSize"));
        List<Cover> covers = mapper.selectCoverAll(map);
        return new PageCover(page.getPageSize(), page.getTotal(), covers);
    }

    public PageSmoke selectSmokeAll(Map<String, Object> map) {
        Page<?> page = PageHelper.startPage((Integer) map.get("pageNum"), (Integer) map.get("pageSize"));
        List<Smoke> smokes = mapper.selectSmokeAll(map);
        return new PageSmoke(page.getPageSize(), page.getTotal(), smokes);
    }

    public SmokeCount getSmokeCount() {
        int w = mapper.selectGtSmokeWarningCount();
        int n = mapper.selectGtSmokeNormalCount();
        return new SmokeCount(w, n);
    }

    public CoverCount getCoverCount() {
        int w = mapper.selectGtCoverWarningCount();
        int n = mapper.selectGtCoverNormalCount();
        return new CoverCount(w, n);
    }


    public CoverAndSmoke getRecentCoverAndSmoke() {
        List<String> recentCover = mapper.getRecentCover();
        List<String> recentSmoke = mapper.getRecentSmoke();
        List<String> dates = mapper.getRecentDates();
        return new CoverAndSmoke(recentCover, recentSmoke, dates);
    }
}
