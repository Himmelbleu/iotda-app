package com.zrfiotda.mappers;

import com.zrfiotda.pojos.Cover;
import com.zrfiotda.pojos.Smoke;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface BaseMapper {

    List<Cover> selectCoverAll(Map<String, Object> map);

    List<Smoke> selectSmokeAll(Map<String, Object> map);

    int selectGtSmokeWarningCount();

    int selectGtSmokeNormalCount();

    int selectGtCoverWarningCount();

    int selectGtCoverNormalCount();

    List<String> getRecentCover();

    List<String> getRecentSmoke();

    @Select("select date from covers limit 10")
    List<String> getRecentDates();
}
