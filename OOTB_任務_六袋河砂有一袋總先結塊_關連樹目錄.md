# 《六袋河砂有一袋總先結塊》關連樹目錄

## 穩定根
- 根任務：《六袋河砂有一袋總先結塊》
- `script_id`: `ootb_low_riversand_20260913`
- 檔案：`OOTB_任務_六袋河砂有一袋總先結塊.md`

## 節點
| 劇名 | script_id | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|
| 六袋河砂有一袋總先結塊 | `ootb_low_riversand_20260913` | — | 根 | — |
| 三段新槽有一段總在夜裡回水 | `ootb_related_returnflow_channel_20260913` | 六袋河砂有一袋總先結塊 | 後傳 | `sand_leak_proven` |

## 關連圖
`六袋河砂有一袋總先結塊:sand_leak_proven → 三段新槽有一段總在夜裡回水`

## 共同背景基線
照江近郊河埠的原六袋河砂受潮事件確由舊洗桶木槽榫縫滲水造成；六袋進倉時同批乾燥，船工沒有偷換濕砂。這些客觀事實不得由後作改寫。

## branch-specific state
- `sand_leak_proven`：原滲水機制已被證明、河砂已保住、責任已釐清；可進入《三段新槽有一段總在夜裡回水》。
- `sand_saved_only`：只保住當日河砂而未完整釐清責任；目前不開啟本後傳。

## 可累積 state
- `returnflow_repaired`：新槽夜間回水機制已證明，止回板墊石正式復位。
- `returnflow_contained`：回水機制已證明並暫時控制，正式復石仍待完成。

## 互斥 state
同一次《三段新槽有一段總在夜裡回水》結案只記錄一個主要 `ending_id`；`returnflow_repaired`、`returnflow_contained`、`returnflow_withdrawn` 互斥。

## ending/state → 後續映射
- `sand_leak_proven` → 可進入《三段新槽有一段總在夜裡回水》。
- `sand_saved_only` → 不滿足目前後傳前置。
- 後傳三個 ending 目前均無已建立後續。

## 多來源條件
目前沒有多來源節點。

## 維護註記
前作泥作匠在後作使用 `<NPC#1@六袋河砂有一袋總先結塊: 姓?-名?>`。若個別桌存檔令其不可用，後作正文已提供泥作行現任工頭作 GM 回歸代用品；代用品只交付既有拆槽工單，不改寫前作人物狀態或新造前作結局。
