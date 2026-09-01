# 《山洪截驛時兩隊救援只能共用一座繩橋》關連樹目錄

> 關係索引文檔；不是資料夾或固定戰役。各劇本正文仍是客觀真相、`ending_id`與持久state的權威來源。

- **根任務**：《山洪截驛時兩隊救援只能共用一座繩橋》
- **根 `script_id`**：`ootb_general_flood_ropebridge_two_rescue_teams_20260831`
- **樹內原則**：只建立本樹內關連；沒有跨樹直接關連。

## 節點與直接關連
| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《山洪截驛時兩隊救援只能共用一座繩橋》 | `ootb_general_flood_ropebridge_two_rescue_teams_20260831` | — | 根任務／洪災救援 | 無 |
| 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》 | `ootb-linked-flood-inn-four-bridge-stakes-old-rope-001` | 《山洪截驛時兩隊救援只能共用一座繩橋》 | 後續／洪災後復路工程與救援器材交接後果 | 非必要；可獨立運行 |
| 《山驛放行前兩捆舊繩都掛著同一枚回收牌》 | `ootb-linked-flood-inn-two-rope-bundles-same-recovery-tag-001` | 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》 | 後續／復路收尾與救援繩具回收交接 | 非必要；可獨立運行 |

## 關連圖
```text
山洪截驛時兩隊救援只能共用一座繩橋
└─→ 山驛復路前四根橋樁有一根還纏著洪夜舊繩
    └─→ 山驛放行前兩捆舊繩都掛著同一枚回收牌
```

## 共同背景基線
- 根任務的山驛與河谷是劇本局部地點，不因此新增Handbook固定地名、行政層級或具名勢力。
- 山洪、受損石橋、洪夜臨時救援繩具與其災後清理可以成為同樹後作的共同事件背景；但根任務哪一隊是否安全、是否有人死亡、PC採取哪條救援路線，仍只由實際`ending_id`與存檔成立，不能升格成全樹共同正史。
- 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》的四根新樁N1–N4、舊臨時樁E、N4晾放、清點錯位及誤綁受力繩都是新事件，不重新判定根任務任何角色的救援決策或責任。
- 《山驛放行前兩捆舊繩都掛著同一枚回收牌》的兩捆回收繩R-A／R-B、重複`回-七`牌與未完成重編均是更晚的收尾清點事件；它不把前作任何橋樁、傷亡、事故或角色決策重新判成繩捆混淆原因。
- 後作可以延續「洪水退去後需要復路、復路後需要整理救援／施工器材」的自然世界後果，但不得由此推定某一具體繩捆必定由某位PC使用，除非實際存檔另有明確記錄。
- 樹內節點不要求相同建議等級、R、規模或難度。

## Branch／state路由
### 根任務 → 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》
- `flood_both_groups_safe`：只形成救援成功與角色可被驛站辨認的公開overlay；後作首次提出洪夜舊樁疑點時，領班較易直接停手查驗。不得推定E就是某位PC曾加固的樁。
- `flood_partial_rescue`：只形成驛站對再次冒險較敏感的程序overlay；後作只要提出一項可觀察異常即可短暫停工。不得把前作傷亡歸因到後作NPC。
- `flood_rescue_breakdown`：根任務曾轉入收殮與封路；後作的世界時點固定在水退、收殮完成並正式啟動復路後，且領班更重視書面放行。不得重置前作結果。
- `flood_rescue_abandoned`：根任務救援曾由驛站收回現場調度；後作只保留驛站自行完成封路與災後處置這一公開背景，首次停工門檻依無前作紀錄基線處理，不把前作角色離場改寫成本篇任何NPC責任。
- 無前作紀錄：後作使用自身無前作基線，只確立近期普通山洪、受損石橋、洪夜臨時救援樁與災後復路；不指定任何根任務ending已發生。
- 四個ending彼此互斥；它們只作開場overlay，不改寫後作固定真相。

### 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》 → 《山驛放行前兩捆舊繩都掛著同一枚回收牌》
- `mountain_inn_rebuild_anchor_traced=true`：前作逐樁查驗留有舊受力繩纖維樣本；新篇首次比對高張力舊繩時可直接取得相容樣本，不改R-A／R-B固定身分。
- `mountain_inn_rebuild_anchor_replaced=true`：前作換樁工單保留拆繩時刻；新篇查簿時可額外知道高張力舊繩何時應進退役堆，不自動指出哪一捆。
- `mountain_inn_rebuild_handoff_clarified=true`：前作已建立逐樁交接；新篇管事見「一牌掛兩捆」時可直接暫停選繩20分鐘，不需先說服。
- `mountain_inn_rebuild_incident=true`：山驛對再發器材事故特別敏感；新篇只要指出一項可見磨傷或號牌矛盾，即可先暫停放行20分鐘。
- 上述state為false或無前作紀錄：新篇使用自身無前作基線；近期洪災、復路完成最低安全條件與器材清點仍成立，但不指定任何前作ending／state已發生。
- 四項state只改資訊成本、停工門檻與程序，不改R-A是應退役高張力舊繩、R-B只可作非承重導繩、或重複牌來自未完成重編的固定真相。

## 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》新增持久state
- `mountain_inn_rebuild_anchor_traced`：舊樁E與新樁N1–N4的身份鏈是否已可靠查明。
- `mountain_inn_rebuild_anchor_replaced`：錯誤受力點是否已由安全新樁／同規格重打樁替換並完成可用施工。
- `mountain_inn_rebuild_handoff_clarified`：逐樁號—位置—用途的交接是否已建立。
- `mountain_inn_rebuild_incident`：該篇是否已發生可觀察的試載／重載事故、毀證、傷人或其他正文定義的事故結果。
- 以上四項可按客觀結果組合成立；除正文明列的布林狀態外，不額外創造人物有罪、永久制度改革或整條驛路安全的推論。

## 《山驛放行前兩捆舊繩都掛著同一枚回收牌》新增持久state
- `mountain_inn_rope_identity_traced`：兩捆回收繩的身分／用途鏈是否已可靠查明。
- `mountain_inn_rope_retired`：應退役的R-A是否已明確退出安全用途。
- `mountain_inn_rope_handoff_clarified`：是否已建立「一捆一號＋用途」的逐捆交接紀錄。
- `mountain_inn_rope_misuse_incident`：R-A是否曾被誤作橋頭安全導繩並發生斷裂／混亂事故。
- 以上state只保存新篇正文客觀成立的結果，不把「可續用」R-B升格成永久承重認證。

## 主要ending／state → 後續映射
### 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》
- `flood-rebuild-four-stakes-cleared`：通常建立`mountain_inn_rebuild_anchor_traced=true`、`mountain_inn_rebuild_anchor_replaced=true`、`mountain_inn_rebuild_handoff_clarified=true`、`mountain_inn_rebuild_incident=false`。
- `flood-rebuild-four-stakes-safe-hold`：固定`mountain_inn_rebuild_anchor_replaced=false`；其餘依終局客觀成立內容保存。
- `flood-rebuild-four-stakes-seized`：固定`mountain_inn_rebuild_incident=true`；其餘依接管前客觀成立內容保存。
- `flood-rebuild-four-stakes-abandon`：只保存離場前已客觀成立內容，不自動補成查明。

### 《山驛放行前兩捆舊繩都掛著同一枚回收牌》
- `rope-cleared`：建立`mountain_inn_rope_identity_traced=true`、`mountain_inn_rope_retired=true`、`mountain_inn_rope_handoff_clarified=true`、`mountain_inn_rope_misuse_incident=false`。
- `rope-safe-hold`：固定`mountain_inn_rope_retired=false`、`mountain_inn_rope_misuse_incident=false`；`mountain_inn_rope_identity_traced`與`mountain_inn_rope_handoff_clarified`依終局客觀成立內容保存。
- `rope-misused`：固定`mountain_inn_rope_misuse_incident=true`；其餘依事故前客觀成立內容保存。
- `rope-abandon`：只保存離場前已客觀成立內容，不自動補成查明、退役或事故。
- 本樹目前任何ending都不自動關閉其他未來節點；未來後作若實際依賴這些state，必須在其正文另列直接來源與可達條件。

## 多來源與互斥
- 本樹目前沒有多來源節點；新篇只直接依賴其上一節點，不因共同背景再把根任務列為第二個直接來源。
- 根任務四個主要ending互斥，但第一後作接受任一ending或無紀錄；不同ending不會被拼成同一存檔背景。
- 後兩篇的布林持久state可依正文客觀結果組合成立；未被正文定義為互斥者不因作者直覺自動互斥。

## 維護
新增、刪除或修改樹內直接關連、`ending_id`／持久state路由或共同背景時，同步更新本檔。劇本檔維持原路徑，不建立同名資料夾、不搬檔；本索引不得創造正文未成立的新前置或新正史。