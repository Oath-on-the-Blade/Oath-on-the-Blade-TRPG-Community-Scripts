# 《三份鹽引只認兩枚官印》關連樹目錄

> 關係索引文檔；不是資料夾或固定戰役。各劇本正文仍是客觀真相與 state 的權威來源。

- **根任務**：《三份鹽引只認兩枚官印》
- **根 `script_id`**：`ootb-salt-permits-two-seals`

## 節點與直接關連

| 劇本 | `script_id` | 直接來源 | 關連定位 | 前作要求 |
|---|---|---|---|---|
| 《三份鹽引只認兩枚官印》 | `ootb-salt-permits-two-seals` | — | 根任務 | 無 |
| 《退倉單上第三船的領訖時辰早了一刻》 | `ootb-linked-salt-return-receipt-001` | 《三份鹽引只認兩枚官印》 | 後續／退倉交接與領訖責任 | 非必要 |

## 關連圖

```text
三份鹽引只認兩枚官印
└─→ 退倉單上第三船的領訖時辰早了一刻
```

## 共同背景基線
- 地點維持江南道同一座可自訂名稱的運河府城；地方官署、鹽運碼頭、官倉與普通船戶均為地方運作單位，不因此新增 Handbook 未定義的常設高層組織。
- 根任務已確立的三份鹽引均為真、舊簿重抄錯頁及地方官署程序責任不得被後作改寫成偽引或私鹽真案。
- 後作的退倉單預填、換鎖延誤、兩包破袋鹽與搬移責任均為新事件，不把根任務 NPC 或錯頁行為強行認定為同一責任來源。
- 根任務若未在角色紀錄中發生，後作使用自己的無前作基線，仍可完整獨立運行。

## branch-specific state
### 根任務
- `seals-restored`：第6小時前證明 A+B，官署補正並放船；第三船未因該案完成入倉。
- `truth-after-tide`：第6小時後證明 A+B；第三船曾完成入倉，翌日需退還；45兩為前作應收債權。
- `seizure-stands`：本篇時限內未成立 A+B；三日後可由官署自行發現錯頁再進入後作基線。
- `salt-permits-abandoned`：沒有可直接承接的已確認責任 state；後作採無前作基線。

### 《退倉單上第三船的領訖時辰早了一刻》
- `salt_return_receipt_corrected=true/false`：退倉單是否已完成責任更正。
- `salt_return_two_bags_recovered=true/false`：兩包破袋鹽是否在本篇時限內被找回並保全。
- `salt_return_boatman_liability=false/unresolved/true`：船戶對兩包短少的責任是否排除、未決或被錯誤記入。

## 可累積 state
- 根任務的公開程序錯誤已被官署知悉，可與後作的退倉更正同時成立。
- 前作45兩應收債權與後作35兩／20兩新委託酬勞可以同時存在，但必須分開結算，不得重複計算。

## 互斥 state
- 同一次根任務紀錄只能有一個主要 `ending_id`。
- 同一次後作紀錄中，`salt_return_boatman_liability=false`、`unresolved`、`true` 互斥。
- `salt_return_receipt_corrected=true` 與同一次事件的 `salt_return_boatman_liability=true` 不可同時成立。

## ending/state → 後續映射
- `seals-restored` → 後作可運行，但固定為三日後另一批同船號的補退貨程序；不得聲稱根任務第三船已入倉。
- `truth-after-tide` → 後作可直接作翌日退倉程序；保留前作45兩應收債權。
- `seizure-stands` → 三日後官署自行發現錯頁並准退貨，再進入後作。
- 無前作紀錄／`salt-permits-abandoned` → 後作使用無前作基線。

## 多來源條件
目前沒有多來源節點；後作只有根任務一個直接來源。

## 維護註記
- 新後作若讀取退倉單更正、兩包鹽去向或船戶責任，必須把《退倉單上第三船的領訖時辰早了一刻》列為直接來源。
- 不得把普通船戶、腳夫、官倉或簿房自行建立成相對名譽對象；社會名譽仍只使用 Handbook 正式對象。
- 目錄只記錄正文已存在的 ending/state；不得用目錄創造新的前置、物權或正史。