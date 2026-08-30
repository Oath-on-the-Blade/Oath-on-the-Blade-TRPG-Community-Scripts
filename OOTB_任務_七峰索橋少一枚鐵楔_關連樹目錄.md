# 《七峰索橋少一枚鐵楔》關連樹目錄

> 關係索引文檔；不是資料夾或固定戰役。各劇本正文仍是客觀真相與 state 的權威來源。

- **根任務**：《七峰索橋少一枚鐵楔》
- **根 `script_id`**：`ootb-random-tianyue-wedge-001`

## 節點與直接關連

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《七峰索橋少一枚鐵楔》 | `ootb-random-tianyue-wedge-001` | — | 根任務 | 無 |
| 《山務院少了兩行驗貨記》 | `ootb-linked-missing-inspection-lines-001` | 《七峰索橋少一枚鐵楔》 | 後續／揭曉 | 非必要 |
| 《石泉驛鐵作門前掛了十二塊空牌》 | `ootb-linked-shiquan-empty-work-tags-001` | 《山務院少了兩行驗貨記》 | 後續／制度與債務後果 | 非必要 |
| 《外峰六枚驗橋印有一枚蓋早了》 | `ootb-linked-tianyue-bridge-seal-001` | 《七峰索橋少一枚鐵楔》 | 平行式後續／驗橋程序分支 | 非必要 |
| 《外峰新橋夜簿少了一趟車》 | `ootb-linked-tianyue-night-ledger-001` | 《外峰六枚驗橋印有一枚蓋早了》 | 後續／橋務通行制度後果；另為中等級門派武學特殊獎勵節點 | 非必要 |
| 《外峰新橋下維修吊台卡在半空》 | `ootb-linked-tianyue-bridge-cradle-001` | 《外峰新橋夜簿少了一趟車》 | 後續／橋下維修救援與受力程序後果 | 非必要 |
| 《北坡三張補簽頁有一張早了一刻》 | `ootb-linked-tianyue-backdated-slip-001` | 《外峰新橋夜簿少了一趟車》 | 後續／補簽制度後果 | 非必要 |
| 《外峰三道封橋牌有一道昨夜被翻回去了》 | `ootb-linked-tianyue-bridge-board-001` | 《北坡三張補簽頁有一張早了一刻》 | 後續／橋務交接與分流制度後果 | 非必要 |
| 《南橋卸重棚少了一根記重木籤》 | `ootb-linked-tianyue-southbridge-load-tag-001` | 《外峰三道封橋牌有一道昨夜被翻回去了》 | 後續／南橋貨務與卸重交接後果 | 非必要 |
| 《南橋雨後三條車道有一條先掛了放行牌》 | `ootb-linked-tianyue-southbridge-rainlane-001` | 《南橋卸重棚少了一根記重木籤》 | 後續／南橋貨流與雨後臨時車道交接後果 | 非必要 |
| 《南橋夜修坡腳多了兩車未登記碎石》 | `ootb-linked-tianyue-southbridge-nightfill-001` | 《南橋雨後三條車道有一條先掛了放行牌》 | 後續／南橋雨後坡腳修補與夜間收料交接後果 | 非必要 |
| 《南橋晨運一輛藥車在坡口歪了半尺》 | `ootb-linked-tianyue-southbridge-medicine-cart-001` | 《南橋夜修坡腳多了兩車未登記碎石》 | 後續／南橋復路後晨運安全與貨車裝載責任 | 非必要 |
| 《南橋午前兩輛空車在回轉坪頂住了》 | `ootb-linked-tianyue-southbridge-turning-yard-001` | 《南橋晨運一輛藥車在坡口歪了半尺》 | 後續／南橋晨運後回轉秩序與車具安全責任 | 非必要 |
| 《南橋車作棚三根換下車轅有一根沒有裂口》 | `ootb-linked-tianyue-southbridge-shaft-rack-001` | 《南橋午前兩輛空車在回轉坪頂住了》 | 後續／南橋車具查驗與維修記錄責任 | 非必要 |
| 《南橋試車坡四道輪痕有一道逆著上坡》 | `ootb-linked-tianyue-southbridge-reverse-track-001` | 《南橋車作棚三根換下車轅有一根沒有裂口》 | 後續／南橋試車程序、坡道安全與記錄責任 | 非必要 |
| 《南橋坡下回收坪三枚止輪楔有一枚插反了》 | `ootb-linked-tianyue-southbridge-recovery-chock-001` | 《南橋試車坡四道輪痕有一道逆著上坡》 | 後續／南橋回收坪止輪程序、車位交接與現場記錄責任 | 非必要 |
| 《南橋回收坪兩塊車位牌疊在同一格》 | `ootb-linked-tianyue-southbridge-bay-tag-001` | 《南橋坡下回收坪三枚止輪楔有一枚插反了》 | 後續／回收坪車位標示、交接與放車程序後果 | 非必要 |

## 關連圖

```text
七峰索橋少一枚鐵楔
├─→ 山務院少了兩行驗貨記
│   └─→ 石泉驛鐵作門前掛了十二塊空牌
└─→ 外峰六枚驗橋印有一枚蓋早了
    └─→ 外峰新橋夜簿少了一趟車
        ├─→ 外峰新橋下維修吊台卡在半空
        └─→ 北坡三張補簽頁有一張早了一刻
            └─→ 外峰三道封橋牌有一道昨夜被翻回去了
                └─→ 南橋卸重棚少了一根記重木籤
                    └─→ 南橋雨後三條車道有一條先掛了放行牌
                        └─→ 南橋夜修坡腳多了兩車未登記碎石
                            └─→ 南橋晨運一輛藥車在坡口歪了半尺
                                └─→ 南橋午前兩輛空車在回轉坪頂住了
                                    └─→ 南橋車作棚三根換下車轅有一根沒有裂口
                                        └─→ 南橋試車坡四道輪痕有一道逆著上坡
                                            └─→ 南橋坡下回收坪三枚止輪楔有一枚插反了
                                                └─→ 南橋回收坪兩塊車位牌疊在同一格
```

## 共同背景基線
- 天嶽七峰外圍的橋材、驗貨、驗橋與橋務通行責任文化可延續；不得因此新增世界知識庫未定義的常設高層機構。
- 後作可承接外峰更注意驗收／橋務程序的公開後果，但不得把前作某枚錯楔、某批材料、某次錯印、補簽或 NPC 強行認定為後作案件同一來源，除非實際存檔已建立該 state。
- 《石泉驛…》承接《山務院…》供應／帳務後果，不重新改判前作責任。
- 《外峰新橋夜簿…》只承接新橋已投入日常運作與程序警覺；其夜間通行、銅扣失竊與責任者均為新事件。
- 《外峰新橋下維修吊台卡在半空》只承接夜簿可保存的補記、公共零件與緊急通行程序 state；吊台事故本身為新事件。
- 《北坡三張補簽頁…》只承接夜間急行補簽與見證程序；改頁、借號、藥貨與私鹽為新事件。
- 《外峰三道封橋牌…》只承接北坡補簽／見證制度 state；翻牌、護坡沖刷與本篇責任為新事件。
- 《南橋卸重棚少了一根記重木籤》只承接交接透明度、北坡重車封控與橋損 state；失籤、位置牌誤掛、車具支點與責任為新事件。
- 《南橋雨後三條車道有一條先掛了放行牌》只承接木籤、交班、第三車與事故 state；提前掛牌、第一車入道、排水堵塞與雨後土肩為新事件。
- 《南橋夜修坡腳多了兩車未登記碎石》只承接雨後交班、排水、重車限制與事故 state；臨時補料、未登簿、混合料替換與夜班收料為新事件。
- 《南橋晨運一輛藥車在坡口歪了半尺》只承接夜修材料查驗、壞料移除、收料追溯與沉陷 state；偏載、固定不足與晨運責任為新事件。
- 《南橋午前兩輛空車在回轉坪頂住了》只承接藥車／藥貨保全、事故因果與前作結束時清路 state；車轅舊裂、第二車入坪與事後翻牌為新事件；前作 `road_cleared=false` 不永久封死後續世界時間。
- 《南橋車作棚三根換下車轅有一根沒有裂口》只承接回轉坪清障、因果、放行交接與裂轅 state；第三根舊轅隱藏榫肩鬆損、總單簡寫與私人尾款為新事件。
- 《南橋試車坡四道輪痕有一道逆著上坡》只承接車轅缺陷覆核、記錄補正、舊轅封存與爭議 state；受控牽回、煞木間隙、雨後鬆石與試車簿簡寫為新事件。
- 《南橋坡下回收坪三枚止輪楔有一枚插反了》只承接輪痕原因、坡面修復、記錄補正與前作結束時封坡 state；換楔、舊楔錯置、反向插楔、翻牌與解索覆核為新事件；若前作封坡，本篇在後續修復重開後發生。
- 《南橋回收坪兩塊車位牌疊在同一格》只承接回收坪前篇的換楔查明、交接釐清、車位修復與前作結束時封位 state；其受潮晾牌、代掛、兩牌同翻、遠距催放與半解索均為新事件；若前作 `southbridge_recovery_bay_closed=true`，本篇在山務後續修復重開後發生。
- 關連樹節點的任務定位、建議等級、R、規模與難度不要求相同。

## Branch／state 路由
- 《外峰六枚驗橋印…》的根任務 overlay 只改文書查驗耗時、陪同與態度，不決定責任者或橋體安全。
- 《外峰新橋夜簿…》可建立 `night-ledger-gap-explained`、`bridge-fittings-recovered`、`emergency-passage-rule-clarified`；彼此可累積。END-01 的天嶽派武學來源屬角色個人來源，不是全樹 state。
- 《外峰新橋下維修吊台卡在半空》只讀上述三項 state，並可建立 `bridge_cradle_rescue_completed`、`bridge_hoist_failure_traced`、`bridge_cradle_load_rule_clarified`、`bridge_cradle_casualty`。
- 《北坡三張補簽頁…》可建立 `backdated-slip-exposed`、`medicine-consignment-secured`、`witness-chain-preserved`；彼此可累積。
- 《外峰三道封橋牌…》只讀上述北坡 state，並可建立 `outerpeak_bridge_board_handoff_clarified`、`outerpeak_north_bridge_heavy_closed`、`outerpeak_north_bridge_damaged`。
- 《南橋卸重棚少了一根記重木籤》只讀上述 `outerpeak_*` state，並可建立 `southbridge_loadtags_restored`、`southbridge_third_cart_rebalanced`、`southbridge_handoff_traceable`、`southbridge_load_incident`。
- 《南橋雨後三條車道有一條先掛了放行牌》只讀前述南橋卸重 state，並可建立 `southbridge_rainlane_handoff_clarified`、`southbridge_rainlane_drained`、`southbridge_rainlane_heavy_restricted`、`southbridge_rainlane_incident`。
- 《南橋夜修坡腳多了兩車未登記碎石》只讀 `southbridge_rainlane_*`，並可建立 `southbridge_nightfill_materials_verified`、`southbridge_nightfill_badfill_removed`、`southbridge_nightfill_receipt_traceable`、`southbridge_nightfill_incident`。
- 《南橋晨運一輛藥車在坡口歪了半尺》只讀 `southbridge_nightfill_*`，並可建立 `southbridge_medicine_cart_saved`、`southbridge_medicine_cart_cause_traced`、`southbridge_medicine_cart_road_cleared`。
- 《南橋午前兩輛空車在回轉坪頂住了》只讀 `southbridge_medicine_cart_*`，並可建立 `southbridge_turning_yard_cleared`、`southbridge_turning_yard_cause_traced`、`southbridge_turning_yard_handoff_clarified`、`southbridge_turning_yard_incident`。
- 《南橋車作棚三根換下車轅有一根沒有裂口》只讀 `southbridge_turning_yard_*`，並可建立 `southbridge_shaft_hidden_defect_verified`、`southbridge_shaft_record_corrected`、`southbridge_shaft_reuse_blocked`、`southbridge_shaft_dispute_unresolved`。
- 《南橋試車坡四道輪痕有一道逆著上坡》只讀 `southbridge_shaft_*`，並可建立 `southbridge_reverse_track_explained`、`southbridge_test_slope_repaired`、`southbridge_test_record_corrected`、`southbridge_test_slope_closed`。
- 《南橋坡下回收坪三枚止輪楔有一枚插反了》只讀上述四項試車坡 state，並可建立 `southbridge_recovery_chock_swap_traced`、`southbridge_recovery_handoff_clarified`、`southbridge_recovery_bay_repaired`、`southbridge_recovery_bay_closed`。
- 《南橋回收坪兩塊車位牌疊在同一格》只讀上述四項 `southbridge_recovery_*` state；它們只改現場保存態度、交接核對耗時與開場世界時點，不改本篇代掛、同翻、催放或半解索真相。可建立 `southbridge_bay_tag_stack_traced`、`southbridge_bay_tag_handoff_clarified`、`southbridge_bay_tag_bays_reopened`、`southbridge_bay_tag_incident`；只按正文 ending 與實際客觀結果寫入。
- 《山務院…》支線與《外峰…》支線同屬一樹但不自動互斥；只有實際持久 state 衝突才限制先後。

## 主要 ending／state → 後續映射
- 《外峰六枚驗橋印…》任何 ending 或無紀錄都可進《外峰新橋夜簿…》。
- 《外峰新橋夜簿…》任何 ending 或無紀錄都可進《外峰新橋下維修吊台卡在半空》及《北坡三張補簽頁…》；只有實際存在的 state 形成 overlay。
- 《外峰新橋下維修吊台卡在半空》各 ending 只按正文保存完整救援／僅救援／傷亡／接管及已成立查驗，不為其他節點補造 state。
- 《北坡三張補簽頁…》任何 ending 或無紀錄都可進《外峰三道封橋牌…》。
- 《外峰三道封橋牌…》各 ending 分別保存安全交接、只安全封控、橋損事故或離場前已成立內容；任何 ending 或無紀錄都可進《南橋卸重棚少了一根記重木籤》。
- 《南橋卸重棚少了一根記重木籤》各 ending 保存完整車次／交接、安全延後、偏載事故或離場前客觀內容；任何 ending 或無紀錄都可進《南橋雨後三條車道有一條先掛了放行牌》。
- 《南橋雨後三條車道有一條先掛了放行牌》各 ending 保存交班／排水／重車限制、安全分流、事故或離場前內容；任何 ending 或無紀錄都可進《南橋夜修坡腳多了兩車未登記碎石》。
- 《南橋夜修坡腳多了兩車未登記碎石》各 ending 保存材料查驗／壞料移除／收料追溯、安全分料、沉陷事故或離場前內容；任何 ending 或無紀錄都可進《南橋晨運一輛藥車在坡口歪了半尺》。
- 《南橋晨運一輛藥車在坡口歪了半尺》各 ending 保存藥車／藥貨、事故因果、清路或離場前內容；任何 ending 或無紀錄都可進《南橋午前兩輛空車在回轉坪頂住了》，前作 `road_cleared=false` 時只延後到山務恢復正常晨運後。
- 《南橋午前兩輛空車在回轉坪頂住了》各 ending 保存清障、因果、放行交接、裂轅事故或離場前內容；任何 ending 或無紀錄都可進《南橋車作棚三根換下車轅有一根沒有裂口》。
- 《南橋車作棚三根換下車轅有一根沒有裂口》各 ending 保存隱藏缺陷覆核、記錄更正、舊轅禁用、爭議或離場前內容；任何 ending 或無紀錄都可進《南橋試車坡四道輪痕有一道逆著上坡》。
- 《南橋試車坡四道輪痕有一道逆著上坡》各 ending 保存輪痕原因、坡面修復、記錄補正、封坡或接管；任何 ending 或無紀錄都可進《南橋坡下回收坪三枚止輪楔有一枚插反了》，前作封坡只延後到修復重開後。
- 《南橋坡下回收坪三枚止輪楔有一枚插反了》的 `southbridge-recovery-chock-cleared` 建立換楔鏈與交接鏈已釐清、第三車位已修復且重開；`southbridge-recovery-chock-safe-delay` 保存安全封位並按實際保存已成立查驗；`southbridge-recovery-chock-seized` 保存山務接管與本篇結束前已成立結果；`southbridge-recovery-chock-abandon` 只保存離場前客觀成立內容。任何 ending 或無紀錄都可進《南橋回收坪兩塊車位牌疊在同一格》；只有實際存在的 `southbridge_recovery_*` state 形成 overlay，前作不是必要前置，封位 state 只延後到後續修復重開後。
- 《南橋回收坪兩塊車位牌疊在同一格》的 `southbridge-bay-tag-cleared` 建立疊牌鏈、交接鏈已釐清且兩車位重開；`southbridge-bay-tag-safe-delay` 保存安全封位並按實際保存已成立查驗；`southbridge-bay-tag-seized` 保存山務接管、是否發生側移險情與接管前已成立內容；`southbridge-bay-tag-abandon` 只保存離場前客觀成立內容。
- 一個 ending 開啟後續不表示其他同樹節點互斥。

## 維護
新增節點時同步更新本檔；劇本檔維持原路徑，不建立同名資料夾、不搬檔。目錄只索引正文已成立的直接邊、state 與共同背景，不創造新的前置或正史。