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
```

## 共同背景基線
- 天嶽七峰外圍的橋材、驗貨、驗橋與橋務通行責任文化可延續；不得因此新增世界知識庫未定義的常設高層機構。
- 後作可承接外峰更注意驗收／橋務程序的公開後果，但不得把前作某枚錯楔、某批材料、某次錯印、補簽或 NPC 強行認定為後作案件同一來源，除非實際存檔已建立該 state。
- 《石泉驛…》承接《山務院…》留下的供應／帳務後果，不重新改判前作責任。
- 《外峰新橋夜簿…》只承接新橋已投入日常運作與程序警覺；其夜間通行、銅扣失竊與責任者均為新事件。
- 《外峰新橋下維修吊台卡在半空》只承接《外峰新橋夜簿…》可保存的夜間補記、公共零件與緊急通行程序 state；其舊制動楔、重索盤超載、棘輪空跳與吊台事故均為新的橋下維修事件，不回頭改判前作失竊或走私責任。
- 《北坡三張補簽頁…》只承接夜間急行補簽與見證程序；其改頁、借號、藥貨與私鹽均為新事件。
- 《外峰三道封橋牌…》只承接北坡補簽／見證制度留下的有效 state；其昨夜翻牌、護坡沖刷與本篇責任均為新事件，不回頭改判前作。
- 《南橋卸重棚少了一根記重木籤》只承接前篇可保存的交接透明度、北坡重車封控與橋損 state；其失籤、位置牌誤掛、車具支點與責任均為新的南橋貨務事件，不把前篇任何翻牌人或橋損責任改判成本篇原因。
- 《南橋雨後三條車道有一條先掛了放行牌》只承接南橋前篇可保存的木籤、交班、第三車處理與事故 state；其提前掛牌、第一車入道、排水堵塞與雨後土肩軟化均為新的候車坡事件，不回頭改判前作責任。
- 《南橋夜修坡腳多了兩車未登記碎石》只承接雨後前篇可保存的交班、排水、重車限制與事故 state；其臨時補料、未登簿、混合料替換與夜班收料責任均為新的坡腳修補事件，不回頭改判前作責任。
- 關連樹節點的任務定位、建議等級、R、規模與難度不要求相同。

## Branch／state 路由
- 《外峰六枚驗橋印…》的根任務 overlay 只改文書查驗耗時、陪同與態度，不決定責任者或橋體安全。
- 《外峰新橋夜簿…》可建立 `night-ledger-gap-explained`、`bridge-fittings-recovered`、`emergency-passage-rule-clarified`；彼此可累積。
- 《外峰新橋夜簿…》END-01 可讓合資格天嶽派正式門人取得 `〈天風步法〉｜來源：[來自〈天嶽派〉]｜解鎖武學等級至14級`；這是角色個人來源，不是全樹 state。
- 《外峰新橋下維修吊台卡在半空》只直接讀取上述三項 `night-ledger`／`bridge-fittings`／`emergency-passage` state：它們只改補記查閱、合規備件可得性與橋面分流耗時，不改吊台事故真相。
- 《外峰新橋下維修吊台卡在半空》可建立 `bridge_cradle_rescue_completed=true/false`、`bridge_hoist_failure_traced=true/false`、`bridge_cradle_load_rule_clarified=true/false`、`bridge_cradle_casualty=true/false`；只有正文 ending 與實際世界結果成立時寫入，不由目錄補造。
- 《北坡三張補簽頁…》可建立 `backdated-slip-exposed`、`medicine-consignment-secured`、`witness-chain-preserved`；均可累積，不與既有 state 自動互斥。
- 《外峰三道封橋牌…》只讀上述三項北坡 state：`witness-chain-preserved` 影響交班核對耗時，`backdated-slip-exposed` 影響補記透明度，`medicine-consignment-secured` 不改本篇真相。
- 《外峰三道封橋牌…》可建立 `outerpeak_bridge_board_handoff_clarified=true/false`（互斥，以最新合法 ending 為準）、`outerpeak_north_bridge_heavy_closed=true`、`outerpeak_north_bridge_damaged=true`；後兩者是否同時存在按實際 ending 與後續處置保存，不由目錄補造。
- 《南橋卸重棚少了一根記重木籤》只直接讀取 `outerpeak_bridge_board_handoff_clarified`、`outerpeak_north_bridge_heavy_closed`、`outerpeak_north_bridge_damaged`：前者只改交班核對，後兩者只改南橋貨流壓力與山務對冒險試放的容忍度，不改本篇真相。
- 《南橋卸重棚少了一根記重木籤》可建立 `southbridge_loadtags_restored=true`、`southbridge_third_cart_rebalanced=true/false`、`southbridge_handoff_traceable=true/false`、`southbridge_load_incident=true`；只有正文 ending 實際成立時寫入，目錄不補造。
- 《南橋雨後三條車道有一條先掛了放行牌》只直接讀取 `southbridge_loadtags_restored`、`southbridge_handoff_traceable`、`southbridge_third_cart_rebalanced`、`southbridge_load_incident`；它們只改核對耗時、交班可信度與山務對分流／試放的接受度，不改本篇責任或雨後土肩真相。
- 《南橋雨後三條車道有一條先掛了放行牌》可建立 `southbridge_rainlane_handoff_clarified=true/false`（互斥，以最新合法 ending 為準）、`southbridge_rainlane_drained=true/false`、`southbridge_rainlane_heavy_restricted=true`、`southbridge_rainlane_incident=true`；只有正文 ending 實際成立時寫入。
- 《南橋夜修坡腳多了兩車未登記碎石》只直接讀取上述四項 `southbridge_rainlane_*` state；它們只改交班核對、排水施工條件、測試方法與山務／車隊態度，不改本篇兩車材料品質、換料責任或收料真相。
- 《南橋夜修坡腳多了兩車未登記碎石》可建立 `southbridge_nightfill_materials_verified=true/false`、`southbridge_nightfill_badfill_removed=true/false`、`southbridge_nightfill_receipt_traceable=true/false`、`southbridge_nightfill_incident=true`；只有正文 ending 與實際世界結果成立時寫入，不由目錄補造。
- 《山務院…》支線與《外峰…》支線同屬一樹但不自動互斥；只有實際持久 state 衝突才限制先後。

## 主要 ending／state → 後續映射
- 《外峰六枚驗橋印…》任何 ending 或無紀錄都可進入《外峰新橋夜簿…》。
- 《外峰新橋夜簿…》任何 ending 或無紀錄都可進入《外峰新橋下維修吊台卡在半空》；只有實際存在的三項前作 state 形成 overlay，前作不是必要前置。
- 《外峰新橋下維修吊台卡在半空》的 `bridge-cradle-full-rescue` 建立完整救援、故障鏈與本地限載／雙人覆核 state；`bridge-cradle-rescue-only` 保存救援成功但責任與程序未完整釐清；`bridge-cradle-casualty` 保存實際傷亡與事故前已成立查驗；`bridge-cradle-abandon` 只保存離場前客觀成立內容。
- 《外峰新橋夜簿…》任何 ending 或無紀錄都可進入《北坡三張補簽頁…》。
- 《北坡三張補簽頁…》任何 ending 或無紀錄都可進入《外峰三道封橋牌…》；只有已存在的三項 state 形成 overlay，前作不是必要前置。
- 《外峰三道封橋牌…》`bridge-board-safe-handoff` 建立交接已釐清與北坡重車封控；`bridge-board-safe-only` 建立重車封控但交接未釐清；`bridge-board-heavy-incident` 保存實際橋損與已成立調查 state；`bridge-board-abandon` 只保存離場前實際成立內容。
- 《外峰三道封橋牌…》任何 ending 或無紀錄都可進入《南橋卸重棚少了一根記重木籤》；只有實際存在的 `outerpeak_*` state 形成 overlay，前作不是必要前置。
- 《南橋卸重棚少了一根記重木籤》的 `southbridge-loadtag-clear` 建立完整車次與交接 state；`southbridge-loadtag-safe-delay` 依實際處置保存第三車與交接狀態；`southbridge-loadtag-incident` 保存偏載事故及已成立交接；`southbridge-loadtag-abandon` 只保存離場前客觀成立內容。
- 《南橋卸重棚少了一根記重木籤》任何 ending 或無紀錄都可進入《南橋雨後三條車道有一條先掛了放行牌》；只有實際存在的 `southbridge_*` state 形成 overlay，前作不是必要前置。
- 《南橋雨後三條車道有一條先掛了放行牌》的 `southbridge-rainlane-clear` 建立交班釐清、排水處理與重車限制 state；`southbridge-rainlane-safe-only` 保存安全分流與未釐清交班；`southbridge-rainlane-incident` 保存雨後土肩事故與後續限制；`southbridge-rainlane-abandon` 只保存離場前客觀成立內容。
- 《南橋雨後三條車道有一條先掛了放行牌》任何 ending 或無紀錄都可進入《南橋夜修坡腳多了兩車未登記碎石》；只有實際存在的 `southbridge_rainlane_*` state 形成 overlay，前作不是必要前置。
- 《南橋夜修坡腳多了兩車未登記碎石》的 `southbridge-nightfill-traceable` 建立材料已驗、壞料已移除與逐車收料可追溯；`southbridge-nightfill-safe-only` 保存安全分料但收料責任未完全接上；`southbridge-nightfill-incident` 保存坡腳沉陷及實際已成立查驗 state；`southbridge-nightfill-abandon` 只保存離場前客觀成立內容。
- 一個 ending 開啟後續不表示其他同樹節點互斥。

## 維護
新增節點時同步更新本檔；劇本檔維持原路徑，不建立同名資料夾、不搬檔。目錄只索引正文已成立的直接邊、state 與共同背景，不創造新的前置或正史。