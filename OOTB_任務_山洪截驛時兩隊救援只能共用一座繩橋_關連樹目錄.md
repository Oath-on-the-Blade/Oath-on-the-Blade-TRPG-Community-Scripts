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

## 關連圖
```text
山洪截驛時兩隊救援只能共用一座繩橋
└─→ 山驛復路前四根橋樁有一根還纏著洪夜舊繩
```

## 共同背景基線
- 根任務的山驛與河谷是劇本局部地點，不因此新增Handbook固定地名、行政層級或具名勢力。
- 山洪、受損石橋、洪夜臨時救援繩具與其災後清理可以成為同樹後作的共同事件背景；但根任務哪一隊是否安全、是否有人死亡、PC採取哪條救援路線，仍只由實際`ending_id`與存檔成立，不能升格成全樹共同正史。
- 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》的四根新樁N1–N4、舊臨時樁E、N4晾放、清點錯位及誤綁受力繩都是新事件，不重新判定根任務任何角色的救援決策或責任。
- 後作可以延續「洪水退去後需要復路」這一自然世界後果，但不得由此推定前作臨時繩橋是否曾被特定PC加固、哪根具體木樁曾由誰使用，除非前作存檔另有明確記錄。
- 樹內節點不要求相同建議等級、R、規模或難度。

## Branch／state路由
### 根任務 → 《山驛復路前四根橋樁有一根還纏著洪夜舊繩》
- `flood_both_groups_safe`：只形成救援成功與角色可被驛站辨認的公開overlay；後作首次提出洪夜舊樁疑點時，領班較易直接停手查驗。不得推定E就是某位PC曾加固的樁。
- `flood_partial_rescue`：只形成驛站對再次冒險較敏感的程序overlay；後作只要提出一項可觀察異常即可短暫停工。不得把前作傷亡歸因到後作NPC。
- `flood_rescue_breakdown`：根任務曾轉入收殮與封路；後作的世界時點固定在水退、收殮完成並正式啟動復路後，且領班更重視書面放行。不得重置前作結果。
- 無前作紀錄：後作使用自身無前作基線，只確立近期普通山洪、受損石橋、洪夜臨時救援樁與災後復路；不指定任何根任務ending已發生。
- 三個ending彼此互斥；它們只作開場overlay，不改寫後作固定真相。

## 本篇新增持久state
《山驛復路前四根橋樁有一根還纏著洪夜舊繩》依實際ending保存：
- `mountain_inn_rebuild_anchor_traced`：舊樁E與新樁N1–N4的身份鏈是否已可靠查明。
- `mountain_inn_rebuild_anchor_replaced`：錯誤受力點是否已由安全新樁／同規格重打樁替換並完成可用施工。
- `mountain_inn_rebuild_handoff_clarified`：逐樁號—位置—用途的交接是否已建立。
- `mountain_inn_rebuild_incident`：本篇是否已發生可觀察的試載／重載事故、毀證、傷人或其他正文定義的事故結果。
- 以上四項可按客觀結果組合成立；除正文明列的布林狀態外，不額外創造人物有罪、永久制度改革或整條驛路安全的推論。

## 主要ending／state → 後續映射
- `flood-rebuild-four-stakes-cleared`：通常建立`anchor_traced=true`、`anchor_replaced=true`、`handoff_clarified=true`、`incident=false`。
- `flood-rebuild-four-stakes-safe-hold`：固定`anchor_replaced=false`；其餘依終局客觀成立內容保存。
- `flood-rebuild-four-stakes-seized`：固定`incident=true`；其餘依接管前客觀成立內容保存。
- `flood-rebuild-four-stakes-abandon`：只保存離場前已客觀成立內容，不自動補成查明。
- 本篇任何ending目前都不自動關閉未來同樹節點；未來後作若實際依賴上述state，必須在其正文另列直接來源與可達條件。

## 多來源與互斥
- 本樹目前沒有多來源節點。
- 根任務三個主要ending互斥，但後作接受任一ending或無紀錄；不同ending不會被拼成同一存檔背景。
- 本篇四項持久state不因同一ending來源而自動互斥，只按正文客觀條件寫入。

## 維護
新增、刪除或修改樹內直接關連、`ending_id`／持久state路由或共同背景時，同步更新本檔。劇本檔維持原路徑，不建立同名資料夾、不搬檔；本索引不得創造正文未成立的新前置或新正史。
