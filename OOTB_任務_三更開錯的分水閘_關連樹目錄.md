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
| 《三批新閘銷只有兩批有驗記》 | `OOTB_任務_三批新閘銷只有兩批有驗記.md` | `ootb_general_two_of_three_sluice_pins_20260903` | 《三更開錯的分水閘》 | 後傳／分支可選承接 | 無；可獨立運行 |
| 《四箱舊閘銷有一箱總先被領走》 | `OOTB_任務_四箱舊閘銷有一箱總先被領走.md` | `ootb_general_old_sluice_pins_20260923` | 《三批新閘銷只有兩批有驗記》 | 後傳／可選承接 | 無；可獨立運行 |
| 《三張回收單有一張總晚半日入簿》 | `OOTB_任務_三張回收單有一張總晚半日入簿.md` | `ootb_general_late_scrap_receipt_20260923` | 《四箱舊閘銷有一箱總先被領走》 | 後傳／可選承接 | 無；可獨立運行 |
| 《四本秤房日簿有一本總少半頁印泥帳》 | `OOTB_任務_四本秤房日簿有一本總少半頁印泥帳.md` | `ootb_general_missing_ink_ledger_20260924` | 《三張回收單有一張總晚半日入簿》 | 後傳／可選承接 | 無；可獨立運行 |

## 關連圖
```text
《三更開錯的分水閘》
  ↓ 可選 overlay
《三批新閘銷只有兩批有驗記》
  ↓ 可選 overlay
《四箱舊閘銷有一箱總先被領走》
  ↓ 可選 overlay
《三張回收單有一張總晚半日入簿》
  ↓ 可選 overlay
《四本秤房日簿有一本總少半頁印泥帳》
```

## 共同背景基線
- 荊湖道照江外存在雙回閘、水署值房與附近河村；水署負責閘務、工程料件、舊料回收與事故交接。
- 根任務與各後作各自客觀真相保持原樣；後作不追溯改寫前作事故成因、人物認知、物權或既有結算。
- 第二節點的新閘銷、第三節點的舊料清點、第四節點的三聯回收單、第五節點的官秤房季末帳冊均有自身完整真相；無任何前作存檔時皆可由例行公務自然發生。

## branch-specific state
根至第二節點：`sluice_stable_truth`、`sluice_stable_unclear`、`sluice_breach_evacuated` 提供正文所列程序 overlay；`sluice_bought_off`／`sluice_abandoned` 不自動改名譽或准入。

第二至第三節點：`pins_sealed_truth`、`pins_stopped_unclear`、`pins_reworked_after_install` 提供正文所列程序 overlay；`pins_abandoned` 不自動改變態度或名譽。

第三至第四節點：`oldpins_trace_complete`、`oldpins_safe_unclear`、`oldpins_loaded_with_record` 提供正文所列程序 overlay；`oldpins_abandoned` 不自動改變態度、罪責或名譽。

第四至第五節點：
- `receipt_chain_repaired`：第五節點第一次調閱驗印簿與印泥庫領用簿直接獲准，省10分鐘。
- `receipt_safe_unclear`：第五節點第一次要求封存缺頁日簿直接成立，省10分鐘。
- `receipt_paper_truth_only`：只提供曾有文書時刻不一致的調查方向，不證明第五節點責任。
- `receipt_abandoned`：不自動改變態度、罪責或名譽。

第五節點 ending：`inkledger_chain_repaired`、`inkledger_safe_unclear`、`inkledger_paper_truth_only`、`inkledger_abandoned`，效果以該劇本正文為準。

## 可累積 state
- 五篇各自 ending 可在同一角色履歷中保存；後篇只讀明列 overlay。
- 各篇合法官府／民間名譽變化照角色卡保存並可累積。
- 第五節點的缺頁、朱泥封號、補正與責任狀態不改寫前四篇事故真相、料件物權或既有責任。

## 互斥 state
- 每篇同一輪的主要 `ending_id` 彼此互斥；不同篇 ending 可並存，除非正文另有明確衝突。

## ending／state → 後續映射
| 來源 | 條件 | 後作效果 |
|---|---|---|
| 根任務 | 無存檔 | 第二節點使用無前作紀錄基線 |
| 第二節點 | 無存檔 | 第三節點使用舊料例行清點基線 |
| 第三節點 | 無存檔 | 第四節點使用三方回收單例行核帳基線 |
| 第四節點 | 無存檔 | 第五節點使用官秤房季末清點基線 |
| 第四節點 | `receipt_chain_repaired` | 第五節點首次調閱兩份帳簿直接獲准，省10分鐘 |
| 第四節點 | `receipt_safe_unclear` | 第五節點首次封存缺頁日簿直接成立，省10分鐘 |
| 第四節點 | `receipt_paper_truth_only` | 第五節點只取得調查方向，不取得責任證明 |
| 第四節點 | `receipt_abandoned` | 第五節點不自動產生態度、罪責或名譽效果 |

## 多來源條件
目前每個後作只有一個直接來源；不存在 AND／OR 多來源條件。

## 維護註記
- 所有前作均非後作必要前置；無存檔時不得默認任何前作 ending。
- 後作不使用前作 NPC、物件或證物作必要資訊源。
- overlay 只產生正文明列的程序／調查效果，不把前作未證明的責任或物權帶入。
- 若未來新增節點，先讀本目錄及所有實際直接來源全文，再更新本目錄。
- 關連樹成員檔維持 repo 原路徑；不得以資料夾搬動表示樹成員資格。