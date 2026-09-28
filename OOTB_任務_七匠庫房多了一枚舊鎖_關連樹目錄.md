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
| 《千機峽外七張濾布領用籤有一張總在歸檔後多一道折痕》 | `ootb-linked-tianji-filter-cloth-fold-001` | 《千機峽外六桶車脂有一桶總在開封後浮出細木屑》 | 後續／耗材污染覆核後的濾材領用與批次追溯 | 非必要 |
| 《千機峽外八只晾布筐有一只總在入庫後多出半把細砂》 | `ootb-linked-tianji-drying-basket-sand-001` | 《千機峽外七張濾布領用籤有一張總在歸檔後多一道折痕》 | 後續／濾布乾燥覆驗後的晾曬轉運與異物追溯 | 非必要 |

## 關連圖
```text
《七匠庫房多了一枚舊鎖》
  ↓
《千機峽外三張退料單有一張先蓋了收訖》
  ↓
《千機峽外四捆回爐鐵有一捆總重了十二斤》
  ↓
《千機峽外五車回爐鐵有一車總在轉彎後鬆掉一枚輪楔》
  ↓
《千機峽外六桶車脂有一桶總在開封後浮出細木屑》
  ↓
《千機峽外七張濾布領用籤有一張總在歸檔後多一道折痕》
  ↓
《千機峽外八只晾布筐有一只總在入庫後多出半把細砂》
```
以上直接邊均為非必要後續。

## 共同背景基線
- 天機閣山門位於雲東道千機峽；「器有其主，技有其責」為既定理念。
- 千機峽物料院處理舊器件、拆料、交接及修車耗材；器物安全狀態與責任記錄須可追溯。
- 根任務的一枚淘汰舊鎖、待拆木箱與半上力彈簧臂只屬根任務事件；後作不令該舊鎖或木箱重生，也不把任何根任務 ending 偷升格為共同正史。
- 第一後作的甲、乙、丙三匣、三張退料單、突雨、裂輪銷與錯蓋收訖均為該篇新事件。
- 第二後作的甲乙丙丁四捆回爐鐵、校秤鐵餅、換秤台與十二斤差額均為另一宗新事件；不把第一後作任何 ending 升格為共同正史。
- 第三後作的甲乙丙丁戊五輛回爐車、受潮輪轂、粗削備楔與反覆鬆楔均為另一宗新事件；不把第二後作任何 ending 升格為共同正史。
- 第四後作的甲乙丙丁戊己六桶車脂、粗刨臨時攪棒與丁桶木屑污染均為另一宗新事件；不把第三後作任何 ending 升格為共同正史。
- 第五後作的七張領用籤、七包濾布、西窗漏雨與戊包受潮均為另一宗新事件；不把第四後作任何 ending 升格為共同正史。
- 第六後作的八只晾布筐、南曬場積水、鋪砂維修帶、己筐舊竹縫與底層兩幅沾砂均為另一宗新事件；不把第五後作任何 ending 升格為共同正史。

## branch-specific state
根任務 → 第一後作：
- `tianji_lock_resolved`：第一次向物料院查乙匣來源可直接取得來源批號。
- `tianji_lock_hold_for_review`：乙匣增加「待二次核」麻繩標記。
- `tianji_lock_mishandled`：正式單據移交增加一名值守見證。
- `tianji_lock_abandoned`：使用無前作紀錄基線。

第一後作 → 第二後作：
- `tianji_return_chain_restored=true`：第一次查拆料簿時同時取得昨日換秤台記錄。
- `tianji_return_safe_hold=true`：正式更正增加另一名值守覆核及10分鐘程序成本。
- `tianji_return_chain_broken=true`：四捆預先加封；拆繩檢視須盤點人與車戶代表共同見證。
- `tianji_return_abandoned=true` 或無前作紀錄：使用一般轉運棚基線。

第二後作 → 第三後作：
- `tianji_scrap_chain_restored=true`：第一次查車次簿時同時取得昨夜換輪轂時刻與值守簽記。
- `tianji_scrap_safe_hold=true`：丙車預先增加一道停車繩；解除與復原各增加5分鐘。
- `tianji_scrap_chain_broken=true`：五車出棚覆核改為雙人見證；每次試車增加10分鐘程序成本。
- `tianji_scrap_abandoned=true` 或無前作紀錄：使用一般轉運棚基線。

第三後作 → 第四後作：
- `tianji_cart_chain_restored=true`：第一次查修車領用簿時同時取得昨夜丁桶臨時開封時刻與值守簽記。
- `tianji_cart_safe_hold=true`：丁桶預先增加一道「暫勿領用」麻繩封條；解除取樣與復原各增加5分鐘。
- `tianji_cart_chain_broken=true`：六桶領用改為雙人見證；每次正式開封取樣增加10分鐘程序成本。
- `tianji_cart_abandoned=true` 或無前作紀錄：使用一般耗材庫基線。

第四後作 → 第五後作：
- `tianji_grease_chain_restored=true`：第一次查濾布領用簿時同時取得昨夜戊包移位時刻與值守簽記。
- `tianji_grease_safe_hold=true`：戊包預先增加一道「待乾驗」麻繩封條；解除取樣與復原各增加5分鐘。
- `tianji_grease_chain_broken=true`：七包領用改為雙人見證；每次正式拆包檢視增加10分鐘程序成本。
- `tianji_grease_abandoned=true` 或無前作紀錄：使用一般耗材庫基線。

第五後作 → 第六後作：
- `tianji_filter_chain_restored=true`：第一次查曬場交接簿時同時取得今晨己筐離架與入庫的兩個時刻。
- `tianji_filter_safe_hold=true`：己筐預先增加一道「待覆驗」麻繩封條；解除檢視與復原各增加5分鐘。
- `tianji_filter_chain_broken=true`：八筐入庫改為雙人見證；每次正式拆筐檢視增加10分鐘程序成本。
- `tianji_filter_abandoned=true` 或無前作紀錄：使用一般洗布棚／入庫廊基線。

以上 overlay 只改資料成本、附加標記、見證或程序，不改後作核心真相、DC或主要結局可達性。

## 可累積 state
- 各篇已成立的 ending state 可保留作履歷與未來樹內節點讀取。
- 本樹目前沒有要求兩個既有 ending state 同時成立才可開始的節點。

## 互斥 state
每篇同一次運行只保存該篇實際成立的一項：
- 第一後作：`tianji_return_chain_restored`／`tianji_return_safe_hold`／`tianji_return_chain_broken`／`tianji_return_abandoned`。
- 第二後作：`tianji_scrap_chain_restored`／`tianji_scrap_safe_hold`／`tianji_scrap_chain_broken`／`tianji_scrap_abandoned`。
- 第三後作：`tianji_cart_chain_restored`／`tianji_cart_safe_hold`／`tianji_cart_chain_broken`／`tianji_cart_abandoned`。
- 第四後作：`tianji_grease_chain_restored`／`tianji_grease_safe_hold`／`tianji_grease_chain_broken`／`tianji_grease_abandoned`。
- 第五後作：`tianji_filter_chain_restored`／`tianji_filter_safe_hold`／`tianji_filter_chain_broken`／`tianji_filter_abandoned`。
- 第六後作：`tianji_drying_chain_restored`／`tianji_drying_safe_hold`／`tianji_drying_chain_broken`／`tianji_drying_abandoned`。

## ending／state → 後續映射
| 來源 | 後續 | 效果 |
|---|---|---|
| 根任務任一 ending 或無紀錄 | 《千機峽外三張退料單有一張先蓋了收訖》 | 均可開始；按 overlay 執行 |
| 第一後作任一 ending 或無紀錄 | 《千機峽外四捆回爐鐵有一捆總重了十二斤》 | 均可開始；按 overlay 執行 |
| 第二後作任一 ending 或無紀錄 | 《千機峽外五車回爐鐵有一車總在轉彎後鬆掉一枚輪楔》 | 均可開始；按 overlay 執行 |
| 第三後作任一 ending 或無紀錄 | 《千機峽外六桶車脂有一桶總在開封後浮出細木屑》 | 均可開始；按 overlay 執行 |
| 第四後作任一 ending 或無紀錄 | 《千機峽外七張濾布領用籤有一張總在歸檔後多一道折痕》 | 均可開始；按 overlay 執行 |
| 第五後作任一 ending 或無紀錄 | 《千機峽外八只晾布筐有一只總在入庫後多出半把細砂》 | 均可開始；按 overlay 執行 |
| `tianji_drying_chain_restored`／`safe_hold`／`chain_broken`／`abandoned` | 未指定 | 保留為未來可讀取 state |

## 多來源條件
目前沒有多來源節點。第六後作只實際讀取第五後作的劇本專用 state；更早任務僅為同樹共同背景的間接來源，不冒充直接來源。

## 維護註記
- 新增節點前先讀本目錄、所有直接來源全文，以及會影響共同背景或 branch state 的必要樹內劇本。
- 新節點只列實際依賴的直接來源；共享地區、門派或題材不構成直接邊。
- `independent` 且非必要前置的後作必須保留無前作紀錄基線；overlay 不得偷改核心真相或主要結局可達性。
- 任何新增／刪除直接邊、ending/state 路由或共同背景變更，須與劇本正文同步更新本目錄。
- 本目錄不創造正文沒有的正史、物權、NPC 狀態、武學來源或必要前置。
