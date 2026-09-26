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
| 《千機峽外五車回爐鐵有一車總在轉彎後鬆掉一枚輪楔》 | `ootb-linked-tianji-cart-wedge-001` | 《千機峽外四捆回爐鐵有一捆總重了十二斤》 | 後續／回爐交割後的車軸安全與責任追溯 | 非必要 |
| 《千機峽外六桶車脂有一桶總在開封後浮出細木屑》 | `ootb-linked-tianji-grease-shavings-001` | 《千機峽外五車回爐鐵有一車總在轉彎後鬆掉一枚輪楔》 | 後續／車軸安全覆核後的耗材封存與責任追溯 | 非必要 |

## 關連圖
```text
《七匠庫房多了一枚舊鎖》
        ↓ 非必要後續
《千機峽外三張退料單有一張先蓋了收訖》
        ↓ 非必要後續
《千機峽外四捆回爐鐵有一捆總重了十二斤》
        ↓ 非必要後續
《千機峽外五車回爐鐵有一車總在轉彎後鬆掉一枚輪楔》
        ↓ 非必要後續
《千機峽外六桶車脂有一桶總在開封後浮出細木屑》
```

## 共同背景基線
- 天機閣山門位於雲東道千機峽；「器有其主，技有其責」為既定理念。
- 千機峽物料院處理舊器件、拆料、交接及修車耗材；器物安全狀態與責任記錄須可追溯。
- 根任務的一枚淘汰舊鎖、待拆木箱與半上力彈簧臂只屬根任務事件；後作不令該舊鎖或木箱重生，也不把任何根任務 ending 偷升格為共同正史。
- 第一後作的甲、乙、丙三匣、三張退料單、突雨、裂輪銷與錯蓋收訖均為該篇新事件。
- 第二後作的甲乙丙丁四捆回爐鐵、校秤鐵餅、換秤台與十二斤差額均為另一宗新事件；它不把第一後作任何 ending 升格為共同正史。
- 第三後作的甲乙丙丁戊五輛回爐車、受潮輪轂、粗削備楔與反覆鬆楔均為另一宗新事件；它不把第二後作任何 ending 升格為共同正史。
- 第四後作的甲乙丙丁戊己六桶車脂、粗刨臨時攪棒與丁桶木屑污染均為另一宗新事件；它不把第三後作任何 ending 升格為共同正史。

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

第二後作對第三後作的 overlay：
- `tianji_scrap_chain_restored=true`：第一次查車次簿時同時取得昨夜換輪轂時刻與值守簽記。
- `tianji_scrap_safe_hold=true`：丙車預先增加一道停車繩；解除與復原各增加5分鐘。
- `tianji_scrap_chain_broken=true`：五車出棚覆核改為雙人見證；每次試車增加10分鐘程序成本。
- `tianji_scrap_abandoned=true` 或無前作紀錄：使用一般轉運棚基線。

第三後作對第四後作的 overlay：
- `tianji_cart_chain_restored=true`：第一次查修車領用簿時同時取得昨夜丁桶臨時開封時刻與值守簽記。
- `tianji_cart_safe_hold=true`：丁桶預先增加一道「暫勿領用」麻繩封條；解除取樣與復原各增加5分鐘。
- `tianji_cart_chain_broken=true`：六桶領用改為雙人見證；每次正式開封取樣增加10分鐘程序成本。
- `tianji_cart_abandoned=true` 或無前作紀錄：使用一般耗材庫基線。

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

第三後作四項 ending state 互斥：
- `tianji_cart_chain_restored=true`
- `tianji_cart_safe_hold=true`
- `tianji_cart_chain_broken=true`
- `tianji_cart_abandoned=true`

第四後作四項 ending state 互斥：
- `tianji_grease_chain_restored=true`
- `tianji_grease_safe_hold=true`
- `tianji_grease_chain_broken=true`
- `tianji_grease_abandoned=true`

同一篇同一次運行只保存實際成立的一項。

## ending／state → 後續映射
| 來源 | 後續 | 效果 |
|---|---|---|
| 根任務任一 ending 或無紀錄 | 《千機峽外三張退料單有一張先蓋了收訖》 | 均可開始；按 overlay 執行 |
| 第一後作任一 ending 或無紀錄 | 《千機峽外四捆回爐鐵有一捆總重了十二斤》 | 均可開始；按 overlay 執行 |
| 第二後作任一 ending 或無紀錄 | 《千機峽外五車回爐鐵有一車總在轉彎後鬆掉一枚輪楔》 | 均可開始；按 overlay 執行 |
| 第三後作任一 ending 或無紀錄 | 《千機峽外六桶車脂有一桶總在開封後浮出細木屑》 | 均可開始；按 overlay 執行 |
| `tianji_grease_chain_restored` | 未指定 | 保留為未來可讀取 state |
| `tianji_grease_safe_hold` | 未指定 | 保留為未來可讀取 state |
| `tianji_grease_chain_broken` | 未指定 | 保留為未來可讀取 state |
| `tianji_grease_abandoned` | 未指定 | 保留為未來可讀取 state |

## 多來源條件
目前沒有多來源節點。第四後作只實際讀取第三後作的劇本專用 state；更早任務僅為同樹共同背景的間接來源，不冒充直接來源。

## 維護註記
- 新增節點時先讀本目錄、所有直接來源全文，以及會影響共同背景／branch state 的必要樹內劇本，再判斷是否自然形成多來源。
- 四份後作均為 `independent`，各自前作均非必要前置；不得因目錄存在而要求玩家依序跑完整棵樹。
- 根任務是天機閣門派專用任務；目前四份後作是一般任務。關連層不改各篇運行資格。
- 任何未來後作若引用舊鎖、木箱、三匣、四捆、校秤鐵餅、五車、粗削輪楔、六桶車脂、臨時攪棒或人物，必須依實際 ending／receipt／NPC state 判斷是否仍存在與可調取，不得無條件複製。