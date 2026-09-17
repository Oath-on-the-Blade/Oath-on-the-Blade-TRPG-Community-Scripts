# 《三排河埠木樁有一排總先鬆動》關連樹目錄

- 根任務：〈三排河埠木樁有一排總先鬆動〉
- 根 script_id：`OOTB-LOW-RIVER-PILES`
- 根檔案：`OOTB_任務_三排河埠木樁有一排總先鬆動.md`

## 樹內節點

| 劇名 | 檔名／script_id | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|
| 三排河埠木樁有一排總先鬆動 | `OOTB_任務_三排河埠木樁有一排總先鬆動.md` / `OOTB-LOW-RIVER-PILES` | 無 | 根 | 否 |
| 兩艘改道糧船有一艘遲遲未回 | `OOTB_任務_兩艘改道糧船有一艘遲遲未回.md` / `OOTB-REL-RIVER-GRAIN-BOAT` | `OOTB-LOW-RIVER-PILES` | 後傳／承接 | 否；無前作紀錄有獨立基線 |

## 關連圖

`OOTB-LOW-RIVER-PILES` → `OOTB-REL-RIVER-GRAIN-BOAT`

根任務 `END-01`、`END-02`、`END-03` 均可進入後作；無前作紀錄亦可用後作明列的獨立基線進入。

## 共同背景基線

- 河洛道該河埠有三排泊船木樁，下游排曾出現反覆鬆動的安全問題。
- 近日河水較高，河埠仍是洛安支路附近的小型糧貨轉運點。
- 根任務中兩艘預定靠埠的載糧小船及其靠泊安排，會依根任務結局留下不同公開紀錄；後作不得改寫根任務真正成因。

## branch-specific state

- `ROOT_END01_SAFE_AND_CAUSE_KNOWN`：根 `END-01`；兩個安全泊位已確保，短舊樁成因有充分來源確認。
- `ROOT_END02_SAFE_CAUSE_UNSETTLED`：根 `END-02`；泊位安全已處置，但責任鏈不足。
- `ROOT_END03_GRAIN_DIVERTED`：根 `END-03`；危機3時仍無兩個安全泊位，糧船改道或發生擦碰。
- `ROOT_UNKNOWN_BASELINE`：沒有可讀前作紀錄；後作只採「河埠近日曾臨時調整泊位」的公開基線，不指定前作責任或玩家行動。

## 可累積 state

目前無跨節點可獨立累積的額外 state。

## 互斥 state

`ROOT_END01_SAFE_AND_CAUSE_KNOWN`、`ROOT_END02_SAFE_CAUSE_UNSETTLED`、`ROOT_END03_GRAIN_DIVERTED`、`ROOT_UNKNOWN_BASELINE` 四者作為後作開場來源互斥；每次運行只選一個。

## ending／state → 後續映射

- 根 `END-01` → 後作可玩；後作開場較早取得正確泊位維修紀錄。
- 根 `END-02` → 後作可玩；後作開場只有安全處置紀錄，責任資訊不完整。
- 根 `END-03` → 後作可玩；後作開場直接取得改道紀錄。
- 無前作紀錄 → 後作可玩；使用獨立基線，不替前作生成結局。

## 多來源條件

目前後作只有一個直接來源，無 AND／OR 匯流。

## 維護註記

- 後作只讀取根任務的靠泊／改道公開結果，不把前作未證實的責任補成既定事實。
- 後作不得反向改寫根任務兩根短舊樁的客觀成因。
- 若未來新增樹內節點，先檢查是否自然讀取本後作新增的持久 state，再決定直接邊。