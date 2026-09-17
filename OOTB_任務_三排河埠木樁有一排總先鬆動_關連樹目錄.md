# 《三排河埠木樁有一排總先鬆動》關連樹目錄

- 根任務：〈三排河埠木樁有一排總先鬆動〉
- 根 script_id：`OOTB-LOW-RIVER-PILES`
- 根檔案：`OOTB_任務_三排河埠木樁有一排總先鬆動.md`

## 樹內節點

| 劇名 | 檔名／script_id | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|
| 三排河埠木樁有一排總先鬆動 | `OOTB_任務_三排河埠木樁有一排總先鬆動.md` / `OOTB-LOW-RIVER-PILES` | 無 | 根 | 否 |
| 兩艘改道糧船有一艘遲遲未回 | `OOTB_任務_兩艘改道糧船有一艘遲遲未回.md` / `OOTB-REL-RIVER-GRAIN-BOAT` | `OOTB-LOW-RIVER-PILES` | 後傳／承接 | 否；無前作紀錄有獨立基線 |
| 四塊河埠泊牌有一塊總被翻到背面 | `OOTB_任務_四塊河埠泊牌有一塊總被翻到背面.md` / `OOTB-REL-RIVER-BERTH-SIGNS` | `OOTB-LOW-RIVER-PILES` | 平行後續／分支 | 否；無前作紀錄有獨立基線 |

## 關連圖

```text
OOTB-LOW-RIVER-PILES
├─→ OOTB-REL-RIVER-GRAIN-BOAT
└─→ OOTB-REL-RIVER-BERTH-SIGNS
```

根任務 `END-01`、`END-02`、`END-03` 均可進入兩份後作；無前作紀錄亦可使用各後作明列的獨立基線進入。兩份後作不因同源而互斥。

## 共同背景基線

- 河洛道該河埠有三排泊船木樁，下游排曾出現反覆鬆動的安全問題。
- 近日河水較高，河埠仍是洛安支路附近的小型糧貨轉運點。
- 根任務中兩艘預定靠埠的載糧小船及其靠泊安排，會依根任務結局留下不同公開紀錄；後作不得改寫根任務真正成因。
- 河埠在安全問題後新增可翻面泊牌，屬《四塊河埠泊牌有一塊總被翻到背面》的局部後續事實；它不改寫根任務當時的設備狀態。

## branch-specific state

- `ROOT_END01_SAFE_AND_CAUSE_KNOWN`：根 `END-01`；兩個安全泊位已確保，短舊樁成因有充分來源確認。
- `ROOT_END02_SAFE_CAUSE_UNSETTLED`：根 `END-02`；泊位安全已處置，但責任鏈不足。
- `ROOT_END03_GRAIN_DIVERTED`：根 `END-03`；危機3時仍無兩個安全泊位，糧船改道或發生擦碰。
- `ROOT_UNKNOWN_BASELINE`：沒有可讀前作紀錄；後作只採「河埠近日曾臨時調整泊位」的公開基線，不指定前作責任或玩家行動。

## 可累積 state

《兩艘改道糧船有一艘遲遲未回》可新增：
- `GRAIN_BOAT_RECOVERED`
- `CAUSE_CONFIRMED`

《四塊河埠泊牌有一塊總被翻到背面》可新增：
- `BERTH_SIGNS_CLARIFIED`
- `SHALLOW_BERTH_RISK_RECORDED`
- `BERTH_TRAFFIC_STABILIZED`
- `SIGN_FLIP_CAUSE_UNSETTLED`
- `BERTH_SIGN_CONFUSION_PERSISTS`

兩份後作的上述 state 目前沒有互相排斥；若未來新篇同時讀取兩邊，須把實際來源都列為直接來源並明列 AND／OR 條件。

## 互斥 state

`ROOT_END01_SAFE_AND_CAUSE_KNOWN`、`ROOT_END02_SAFE_CAUSE_UNSETTLED`、`ROOT_END03_GRAIN_DIVERTED`、`ROOT_UNKNOWN_BASELINE` 四者作為後作開場來源互斥；每次運行只選一個。

同一篇後作內由不同 ending 產生、描述同一問題最終狀態的 state 依該篇 ending 自然互斥；不同後作之間目前沒有自動互斥。

## ending／state → 後續映射

- 根 `END-01` → 兩份後作均可玩；各篇按正文載入較完整的維修資料。
- 根 `END-02` → 兩份後作均可玩；各篇只載入安全處置紀錄，責任資訊不完整。
- 根 `END-03` → 兩份後作均可玩；各篇可載入改道紀錄。
- 無前作紀錄 → 兩份後作均可玩；各自使用獨立基線，不替前作生成結局。
- `BERTH_SIGNS_CLARIFIED` 等泊牌 state 目前不開啟或關閉《兩艘改道糧船有一艘遲遲未回》。
- `GRAIN_BOAT_RECOVERED`／`CAUSE_CONFIRMED` 目前不開啟或關閉《四塊河埠泊牌有一塊總被翻到背面》。

## 多來源條件

目前兩份後作都只有根任務一個直接來源，無 AND／OR 匯流。若未來任務同時依賴兩份後作的專用 state，必須把兩份都列為直接來源並明列可同時成立的 AND／OR／互斥邏輯。

## 維護註記

- 後作只讀取根任務的靠泊／改道公開結果，不把前作未證實的責任補成既定事實。
- 後作不得反向改寫根任務兩根短舊樁的客觀成因。
- 《四塊河埠泊牌有一塊總被翻到背面》中的新泊牌是根事件之後的地方改善，不代表根任務當時已存在。
- 兩份後作可在同一 campaign 先後發生；除非未來正文建立明確互斥 state，不得把它們視為二選一。
- 若未來新增樹內節點，先檢查是否自然讀取現有後作新增的持久 state，再決定直接邊。