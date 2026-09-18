# 《七匠庫房多了一枚舊鎖》關連樹目錄

> 關係索引文檔；不是資料夾或固定戰役。各劇本正文仍是客觀真相與 state 的權威來源。

- **根任務**：《七匠庫房多了一枚舊鎖》
- **根 `script_id`**：`ootb_tianji_old_lock_20260830`

## 節點與直接關連
| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《七匠庫房多了一枚舊鎖》 | `ootb_tianji_old_lock_20260830` | — | 根任務 | 無 |
| 《千機峽外三張退料單有一張先蓋了收訖》 | `ootb-linked-tianji-return-receipt-001` | 《七匠庫房多了一枚舊鎖》 | 後續／退料交接與實物收訖程序後果 | 非必要 |
| 《千機峽外四捆回爐鐵有一捆總重了十二斤》 | `ootb-linked-tianji-scrap-weight-001` | 《千機峽外三張退料單有一張先蓋了收訖》 | 後續／舊件拆料後的稱重與回爐交割 | 非必要 |

## 關連圖
```text
《七匠庫房多了一枚舊鎖》
        ↓ 非必要後續
《千機峽外三張退料單有一張先蓋了收訖》
        ↓ 非必要後續
《千機峽外四捆回爐鐵有一捆總重了十二斤》
```

## 共同背景基線
- 天機閣山門位於雲東道千機峽；「器有其主，技有其責」為既定理念。
- 千機峽物料院處理舊器件、拆料與交接；器物安全狀態與責任記錄須可追溯。
- 根任務的一枚淘汰舊鎖、待拆木箱與半上力彈簧臂只屬根任務事件；後作不令該舊鎖或木箱重生，也不把任何根任務 ending 偷升格為共同正史。
- 第一後作的甲、乙、丙三匣、三張退料單、突雨、裂輪銷與錯蓋收訖均為該篇新事件。
- 第二後作的甲乙丙丁四捆回爐鐵、校秤鐵餅、換秤台與十二斤差額均為另一宗新事件；它不把第一後作任何 ending 升格為共同正史。

## branch-specific state
根任務對第一後作的 overlay：
- `tianji_lock_resolved`：第一次向物料院查乙匣來源可直接取得來源批號。
- `tianji_lock_hold_for_review`：乙匣增加「待二次核」麻繩標記。
- `tianji_lock_mishandled`：正式單據移交增加一名值守見證。
- `tianji_lock_abandoned`：使用無前作紀錄基線。

第一後作對第二後作的 overlay：
- `tianji_return_chain_restored=true`：第一次查拆料簿時同時取得昨日換秤台記錄。
- `tianji_return_safe_hold=true`：正式更正增加另一名值守覆核及10分鐘程序成本。
- `tianji_return_chain_broken=true`：四捆預先加封；拆繩檢視須盤點人與車戶代表共同見證。
- `tianji_return_abandoned=true` 或無前作紀錄：使用一般轉運棚基線。

以上 overlay 只改資料成本、附加標記、見證或程序，不改後作核心真相、DC或主要結局可達性。

## 可累積 state
- 各篇已成立的 ending state 可保留作履歷與未來樹內節點讀取。
- 本樹目前沒有要求兩個既有 ending state 同時成立才可開始的節點。

## 互斥 state
第一後作四項 ending state 互斥：
- `tianji_return_chain_restored=true`
- `tianji_return_safe_hold=true`
- `tianji_return_chain_broken=true`
- `tianji_return_abandoned=true`

第二後作四項 ending state 互斥：
- `tianji_scrap_chain_restored=true`
- `tianji_scrap_safe_hold=true`
- `tianji_scrap_chain_broken=true`
- `tianji_scrap_abandoned=true`

同一篇同一次運行只保存實際成立的一項。

## ending／state → 後續映射
| 來源 | 後續 | 效果 |
|---|---|---|
| 根任務任一 ending 或無紀錄 | 《千機峽外三張退料單有一張先蓋了收訖》 | 均可開始；按 overlay 執行 |
| 第一後作任一 ending 或無紀錄 | 《千機峽外四捆回爐鐵有一捆總重了十二斤》 | 均可開始；按 overlay 執行 |
| `tianji_scrap_chain_restored` | 未指定 | 保留為未來可讀取 state |
| `tianji_scrap_safe_hold` | 未指定 | 保留為未來可讀取 state |
| `tianji_scrap_chain_broken` | 未指定 | 保留為未來可讀取 state |
| `tianji_scrap_abandoned` | 未指定 | 保留為未來可讀取 state |

## 多來源條件
目前沒有多來源節點。第二後作只實際讀取第一後作的劇本專用 state；根任務僅為同樹共同背景的間接來源，不冒充直接來源。

## 維護註記
- 新增節點時先讀本目錄、所有直接來源全文，以及會影響共同背景／branch state 的必要樹內劇本，再判斷是否自然形成多來源。
- 兩份後作均為 `independent`，各自前作均非必要前置；不得因目錄存在而要求玩家依序跑完整棵樹。
- 根任務是天機閣門派專用任務；目前兩份後作是一般任務。關連層不改各篇運行資格。
- 任何未來後作若引用舊鎖、木箱、三匣、四捆、校秤鐵餅或人物，必須依實際 ending／receipt／NPC state 判斷是否仍存在與可調取，不得無條件複製。