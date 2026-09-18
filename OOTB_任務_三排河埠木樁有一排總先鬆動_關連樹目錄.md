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
| 三本夜泊簿有一本總少半行 | `OOTB_任務_三本夜泊簿有一本總少半行.md` / `OOTB-REL-RIVER-NIGHT-LEDGER` | `OOTB-REL-RIVER-GRAIN-BOAT` + `OOTB-REL-RIVER-BERTH-SIGNS` | 匯流／承接 | 否；可雙來源、單來源或無前作基線 |

## 關連圖

```text
OOTB-LOW-RIVER-PILES
├─→ OOTB-REL-RIVER-GRAIN-BOAT ─┐
└─→ OOTB-REL-RIVER-BERTH-SIGNS ─┼─→ OOTB-REL-RIVER-NIGHT-LEDGER
                                  └─（兩來源可同時累積；單來源／無紀錄亦有合法入口）
```

根任務 `END-01`、`END-02`、`END-03` 均可進入兩份第一層後作；無前作紀錄亦可使用各後作明列的獨立基線。兩份第一層後作不因同源而互斥。《三本夜泊簿有一本總少半行》實際讀取兩份第一層後作的持久 state；兩邊都有紀錄時為 AND 匯流，只有一邊時以該單來源 OR 入口載入，兩邊皆無時使用獨立基線。

## 共同背景基線

- 河洛道該河埠有三排泊船木樁，下游排曾出現反覆鬆動的安全問題。
- 近日河水較高，河埠仍是洛安支路附近的小型糧貨轉運點。
- 根任務中兩艘預定靠埠的載糧小船及其靠泊安排，會依根任務結局留下不同公開紀錄；後作不得改寫根任務真正成因。
- 河埠在安全問題後新增可翻面泊牌，屬《四塊河埠泊牌有一塊總被翻到背面》的局部後續事實；它不改寫根任務當時的設備狀態。
- 河埠後續增設上埠、下埠、巡水三本夜泊簿以追查夜間移泊，屬《三本夜泊簿有一本總少半行》的局部事實；此制度新增不代表較早劇本當時已有三簿。

## branch-specific state

- `ROOT_END01_SAFE_AND_CAUSE_KNOWN`：根 `END-01`；兩個安全泊位已確保，短舊樁成因有充分來源確認。
- `ROOT_END02_SAFE_CAUSE_UNSETTLED`：根 `END-02`；泊位安全已處置，但責任鏈不足。
- `ROOT_END03_GRAIN_DIVERTED`：根 `END-03`；危機3時仍無兩個安全泊位，糧船改道或發生擦碰。
- `ROOT_UNKNOWN_BASELINE`：沒有可讀根任務紀錄；後作只採「河埠近日曾臨時調整泊位」的公開基線，不指定前作責任或玩家行動。

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

《三本夜泊簿有一本總少半行》可新增：
- `NIGHT_LEDGER_FLOW_STABILIZED`
- `NIGHT_LEDGER_CAUSE_CONFIRMED`
- `NIGHT_LEDGER_CAUSE_UNSETTLED`
- `NIGHT_LEDGER_FLOW_UNSTABLE`

第一層兩份後作的 state 沒有互相排斥，故可由夜泊簿節點共同讀取。`NIGHT_LEDGER_CAUSE_CONFIRMED` 與 `NIGHT_LEDGER_CAUSE_UNSETTLED` 描述同一責任鏈的不同確定程度，不在同一結局同時新增；`NIGHT_LEDGER_FLOW_STABILIZED` 可與其中任一者同時成立。

## 互斥 state

`ROOT_END01_SAFE_AND_CAUSE_KNOWN`、`ROOT_END02_SAFE_CAUSE_UNSETTLED`、`ROOT_END03_GRAIN_DIVERTED`、`ROOT_UNKNOWN_BASELINE` 四者作為第一層後作的根開場來源互斥；每次運行只選一個。

同一篇後作內由不同 ending 產生、描述同一問題最終狀態的 state 依該篇 ending 自然互斥。`NIGHT_LEDGER_FLOW_STABILIZED` 與 `NIGHT_LEDGER_FLOW_UNSTABLE` 互斥；`NIGHT_LEDGER_CAUSE_CONFIRMED` 與 `NIGHT_LEDGER_CAUSE_UNSETTLED` 互斥。第一層兩份後作之間沒有自動互斥。

## ending／state → 後續映射

- 根 `END-01`／`END-02`／`END-03` → 兩份第一層後作均可玩，各篇按正文載入相應資料。
- 無根任務紀錄 → 兩份第一層後作均可玩，各自使用獨立基線，不替根任務生成結局。
- `GRAIN_BOAT_RECOVERED` → 夜泊簿節點可直接調取該船回埠後載貨／吃水抄簿；`CAUSE_CONFIRMED` → 可直接知道柳汊灣沉索事故已確認。兩者都不改夜泊簿真相。
- `BERTH_SIGNS_CLARIFIED`／`BERTH_TRAFFIC_STABILIZED` → 夜泊簿節點可直接取得清楚泊位用途／吃水條件抄本；`SHALLOW_BERTH_RISK_RECORDED` → 可直接取得近岸位量水記錄；`SIGN_FLIP_CAUSE_UNSETTLED`／`BERTH_SIGN_CONFUSION_PERSISTS` → 只提供泊牌曾造成誤解的公開資料，不補寫未證實原因。
- 第一層兩邊都有可讀資料時，夜泊簿節點可交叉比對船的吃水／載重與泊位條件，首次核對成本降低；只有一邊時只載入該邊資料；皆無時用夜泊簿正文獨立基線。
- 夜泊簿三個 ending 目前不開啟其他既有節點，也不反向改寫第一層後作。

## 多來源條件

《三本夜泊簿有一本總少半行》有兩個實際直接來源：`OOTB-REL-RIVER-GRAIN-BOAT` 與 `OOTB-REL-RIVER-BERTH-SIGNS`。

- **AND**：同一 campaign 已有兩篇的合法持久 state 時，兩邊資料同時載入；兩組 state 本來可累積，沒有互斥。
- **OR**：只玩過其中一篇時，只載入該篇保存 state；另一邊使用「無該篇紀錄」基線。
- **無紀錄**：兩篇皆無時，本篇仍完整可運行，只知道河埠近日調整過靠泊安排，不指定任何前作 ending。
- 來源 state 只改資訊起點與首次核對成本，不改本篇客觀真相、NPC 動機、DC 或結局可達性。

## 維護註記

- 後作只讀取前作實際保存的靠泊／改道／船況／泊牌資料，不把前作未證實責任補成既定事實。
- 後作不得反向改寫根任務兩根短舊樁的客觀成因。
- 《四塊河埠泊牌有一塊總被翻到背面》的新泊牌與《三本夜泊簿有一本總少半行》的三簿制度都是各自事件時點的地方改善，不得倒灌到更早劇本。
- 第一層兩份後作可在同一 campaign 先後發生；夜泊簿節點正是合法匯流例，必須按實際 state 載入，不能假定兩篇都已玩過。
- 未來新增節點時，先檢查是否實際讀取夜泊簿新增 state；只有真正依賴其專用資料時才列直接邊。