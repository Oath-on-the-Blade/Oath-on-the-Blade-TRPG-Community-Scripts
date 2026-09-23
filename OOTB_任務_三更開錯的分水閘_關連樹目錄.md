# 《三更開錯的分水閘》關連樹目錄

- 穩定根任務：《三更開錯的分水閘》
- 根檔案：`OOTB_任務_三更開錯的分水閘.md`
- 根 `script_id`: `ootb_general_wrong_sluice_20260828`
- `continuity_id`: `ootb_tree_wrong_sluice_20260903`
- 本文件用途：本棵一般關連樹的關係索引；不是可玩劇本。

## 樹內節點
| 劇名 | 檔名 | `script_id` | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|---|
| 《三更開錯的分水閘》 | `OOTB_任務_三更開錯的分水閘.md` | `ootb_general_wrong_sluice_20260828` | 無 | 穩定根 | 無 |
| 《三批新閘銷只有兩批有驗記》 | `OOTB_任務_三批新閘銷只有兩批有驗記.md` | `ootb_general_two_of_three_sluice_pins_20260903` | 《三更開錯的分水閘》 | 後傳／分支可選承接 | 無；可無前作紀錄獨立運行 |
| 《四箱舊閘銷有一箱總先被領走》 | `OOTB_任務_四箱舊閘銷有一箱總先被領走.md` | `ootb_general_old_sluice_pins_20260923` | 《三批新閘銷只有兩批有驗記》 | 後傳／可選承接 | 無；可無前作紀錄獨立運行 |
| 《三張回收單有一張總晚半日入簿》 | `OOTB_任務_三張回收單有一張總晚半日入簿.md` | `ootb_general_late_scrap_receipt_20260923` | 《四箱舊閘銷有一箱總先被領走》 | 後傳／可選承接 | 無；可無前作紀錄獨立運行 |

## 關連圖
```text
《三更開錯的分水閘》
        │
        └──（可選 ending/state overlay；非必要前置）
             ↓
《三批新閘銷只有兩批有驗記》
        │
        └──（可選 ending/state overlay；非必要前置）
             ↓
《四箱舊閘銷有一箱總先被領走》
        │
        └──（可選 ending/state overlay；非必要前置）
             ↓
《三張回收單有一張總晚半日入簿》
```

## 共同背景基線
- 荊湖道照江外存在雙回閘、水署值房與附近河村。
- 水署負責當地閘務、工程料件、舊料回收與事故交接。
- 根任務的客觀事故真相與各 ending 保持原樣；後作不更改其事故成因、人物認知或既有結算。
- 《三批新閘銷只有兩批有驗記》的三批新閘銷事件有自身完整真相；無根任務存檔也可由秋汛前例行換修自然發生。
- 《四箱舊閘銷有一箱總先被領走》的舊料清點發生在換修後；無任何前作存檔時，亦可由水署例行報廢交接自然發生。
- 《三張回收單有一張總晚半日入簿》的三聯錯時發生在舊料回收流程；無任何前作存檔時，亦可由水署例行核對回收船、岸庫與官秤房單據自然發生。

## branch-specific state
根任務 overlay：
- `sluice_stable_truth`：第二節點查簿准入節省10分鐘。
- `sluice_stable_unclear`：第二節點第一次第三批封存交接省10分鐘。
- `sluice_breach_evacuated`：第二節點符合公開驗料條件時可取得村民秩序協助。
- `sluice_bought_off`／`sluice_abandoned`：不自動改名譽或准入。

第二節點 overlay 至第三節點：
- `pins_sealed_truth`：第三節點查閱舊料總簿授權交接省10分鐘。
- `pins_stopped_unclear`：第三節點第一次封存第四箱省10分鐘填表。
- `pins_reworked_after_install`：拆回新銷另箱保存；第一次要求停船可直接成立。
- `pins_abandoned`：不自動改變官府／民間態度。

第三節點 overlay 至第四節點：
- `oldpins_trace_complete`：第四節點第一次調閱回收碼頭三日裝載簿可直接獲准，省10分鐘。
- `oldpins_safe_unclear`：第四節點第一次要求封存爭議第三聯可直接成立，省10分鐘填表。
- `oldpins_loaded_with_record`：第四節點核對第一組船載時刻省10分鐘；不直接證明誰延遲入簿。
- `oldpins_abandoned`：不自動改變態度、罪責或名譽。

第四節點 ending：`receipt_chain_repaired`、`receipt_safe_unclear`、`receipt_paper_truth_only`、`receipt_abandoned`，其效果以該劇本正文為準。

## 可累積 state
- 四篇各自 ending 可在同一角色履歷中保存；後篇只讀明列 overlay，不追溯改寫前篇。
- 各篇合法官府／民間名譽變化照角色卡保存並可累積。
- 第三節點的第四箱封存、追回舊銷數、補單責任與民用設施安全狀態不改寫前兩篇既有NPC或物件狀態。
- 第四節點的晚送、回填、第四批現場複核與程序補正狀態不改寫前三篇事故真相、料件物權或既有責任。

## 互斥 state
- 同一輪根任務主要 `ending_id` 依原劇本互斥。
- 同一輪第二節點四個主要 `ending_id` 互斥。
- 同一輪第三節點四個主要 `ending_id` 互斥。
- 同一輪第四節點四個主要 `ending_id` 互斥。

## ending／state → 後續映射
| 來源 | 條件 | 後作效果 |
|---|---|---|
| 根任務 | 無存檔 | 第二節點使用無前作紀錄基線 |
| 根任務 | `sluice_stable_truth` | 第二節點查簿准入省10分鐘 |
| 根任務 | `sluice_stable_unclear` | 第二節點首次第三批封存交接省10分鐘 |
| 根任務 | `sluice_breach_evacuated` | 第二節點可在條件成立時取得村民秩序協助 |
| 第二節點 | 無存檔 | 第三節點使用舊料例行清點基線 |
| 第二節點 | `pins_sealed_truth` | 第三節點查舊料總簿授權交接省10分鐘 |
| 第二節點 | `pins_stopped_unclear` | 第三節點首次封存第四箱省10分鐘 |
| 第二節點 | `pins_reworked_after_install` | 第三節點第一次要求停船可直接成立 |
| 第二節點 | `pins_abandoned` | 不自動產生態度或名譽效果 |
| 第三節點 | 無存檔 | 第四節點使用三方回收單例行核帳基線 |
| 第三節點 | `oldpins_trace_complete` | 第四節點第一次調閱三日裝載簿直接獲准，省10分鐘 |
| 第三節點 | `oldpins_safe_unclear` | 第四節點第一次封存爭議第三聯直接成立，省10分鐘 |
| 第三節點 | `oldpins_loaded_with_record` | 第四節點核對第一組船載時刻省10分鐘 |
| 第三節點 | `oldpins_abandoned` | 不自動產生態度、罪責或名譽效果 |

## 多來源條件
目前每個後作只有一個直接來源；不存在 AND／OR 多來源條件。

## 維護註記
- 前作均不是後作必要前置；無存檔時不得默認任何前作 ending。
- 後作不使用前作NPC作必要資訊源，也不把前作物件／證物變成本篇必要條件。
- 第四節點讀取第三節點 ending 時只套用明列的程序時間／准入 overlay；不得把前作未證明的責任或物權帶入。
- 若未來新增節點，先讀本目錄及所有實際直接來源全文，再更新本目錄。
- 關連樹成員檔維持 repo 原路徑；不得以資料夾搬動表示樹成員資格。