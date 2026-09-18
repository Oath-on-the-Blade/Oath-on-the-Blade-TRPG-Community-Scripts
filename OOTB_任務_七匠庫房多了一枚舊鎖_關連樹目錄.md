# 《七匠庫房多了一枚舊鎖》關連樹目錄

> 關係索引文檔；不是資料夾或固定戰役。各劇本正文仍是客觀真相與 state 的權威來源。

- **根任務**：《七匠庫房多了一枚舊鎖》
- **根 `script_id`**：`ootb_tianji_old_lock_20260830`

## 節點與直接關連
| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《七匠庫房多了一枚舊鎖》 | `ootb_tianji_old_lock_20260830` | — | 根任務 | 無 |
| 《千機峽外三張退料單有一張先蓋了收訖》 | `ootb-linked-tianji-return-receipt-001` | 《七匠庫房多了一枚舊鎖》 | 後續／退料交接與實物收訖程序後果 | 非必要 |

## 關連圖
```text
《七匠庫房多了一枚舊鎖》
        ↓ 非必要後續
《千機峽外三張退料單有一張先蓋了收訖》
```

## 共同背景基線
- 天機閣山門位於雲東道千機峽；「器有其主，技有其責」為既定理念。
- 千機峽物料院處理舊器件、拆料與交接；器物安全狀態與責任記錄須可追溯。
- 根任務的一枚淘汰舊鎖、待拆木箱與半上力彈簧臂只屬根任務事件；後作不令該舊鎖或木箱重生，也不把任何根任務 ending 偷升格為共同正史。
- 後作的甲、乙、丙三匣、三張退料單、突雨、裂輪銷與錯蓋收訖均為新事件。

## branch-specific state
根任務可接受的既有 ending／狀態：
- `tianji_lock_resolved`：後作第一次向物料院查乙匣來源可直接取得來源批號。
- `tianji_lock_hold_for_review`：後作乙匣增加「待二次核」麻繩標記。
- `tianji_lock_mishandled`：後作正式單據移交增加一名值守見證。
- `tianji_lock_abandoned`：後作使用無前作紀錄基線。

上述 overlay 只改准入、資料成本或附加標記；不改後作核心真相、DC 或結局可達性。

## 可累積 state
目前無跨兩篇必須累積的 state。後作完成後可保存其自身結果供未來節點讀取。

## 互斥 state
後作四項 ending state 互斥：
- `tianji_return_chain_restored=true`
- `tianji_return_safe_hold=true`
- `tianji_return_chain_broken=true`
- `tianji_return_abandoned=true`
同一次運行只保存實際成立的一項。

## ending／state → 後續映射
| 來源 | 後續 | 效果 |
|---|---|---|
| 根任務任一 ending 或無紀錄 | 《千機峽外三張退料單有一張先蓋了收訖》 | 均可開始；按上方 overlay 執行 |
| `tianji_return_chain_restored` | 未指定 | 保留為未來可讀取 state |
| `tianji_return_safe_hold` | 未指定 | 保留為未來可讀取 state |
| `tianji_return_chain_broken` | 未指定 | 保留為未來可讀取 state |
| `tianji_return_abandoned` | 未指定 | 保留為未來可讀取 state |

## 多來源條件
目前沒有多來源節點；新後作只有根任務一個直接來源。

## 維護註記
- 本樹目前只有兩個節點；新增節點時先讀兩篇正文與本目錄，再判斷是否自然形成多來源。
- 後作為 `independent`，根任務不是必要前置；不得因目錄存在而要求玩家先跑根任務。
- 根任務是天機閣門派專用任務；後作是一般任務。關連層不改兩篇各自運行資格。
- 任何未來後作若引用根任務舊鎖、木箱或人物，必須依實際 ending／receipt／NPC state 判斷是否仍存在與可調取，不得無條件複製。