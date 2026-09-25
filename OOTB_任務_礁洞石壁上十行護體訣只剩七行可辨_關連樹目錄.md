# 《礁洞石壁上十行護體訣只剩七行可辨》關連樹目錄

- 根任務：《礁洞石壁上十行護體訣只剩七行可辨》
- 根 `script_id`：`ootb_martial_canglong_cave_20260924`

## 樹內節點
| 劇名 | 檔名／script_id | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|
| 《礁洞石壁上十行護體訣只剩七行可辨》 | `OOTB_任務_礁洞石壁上十行護體訣只剩七行可辨.md`／`ootb_martial_canglong_cave_20260924` | 無 | 根任務 | 無 |
| 《三份礁洞拓本有一份多出第八行》 | `OOTB_任務_三份礁洞拓本有一份多出第八行.md`／`ootb_related_cave_eighth_line_20260924` | 根任務 | 後傳 | `cave_formula_rebuilt OR cave_formula_saved`，且仍有可核對七行材料 |

## 關連圖
`根:cave_formula_rebuilt OR cave_formula_saved → 三份礁洞拓本有一份多出第八行`

`cave_formula_lost` 且全部可核對材料永久失去時，後傳不可達。

## 共同背景基線
礁洞材料的可驗證內容只支持【龍鱗護體神功】至10級的有限門派外來源；不帶 `[來自蒼龍門]`，不提供蒼龍門身份、引薦或11級以上來源。石壁、拓本與角色實際取得狀態依根任務結算保存。後傳中的「第八行」不改寫此共同背景。

## branch-specific state
- `cave_formula_rebuilt`：至少一份完整七行拓本保全；合資格角色可能各自建立至10級來源。
- `cave_formula_saved`：石壁或拓片被保全，未建立武學來源。
- `cave_formula_lost`：若全部可核對材料永久失去，後傳不可開始。

## 可累積 state
根任務中角色個別是否已建立【龍鱗護體神功】來源，可與後傳任何 ending 同時存在；後傳不得改寫其他角色的既有來源。

## 互斥 state
`cave_formula_rebuilt`、`cave_formula_saved`、`cave_formula_lost` 作為根任務 ending 互斥。後傳的 `eighth_line_exposed`、`eighth_line_contained`、`eighth_line_circulated` 三者互斥。

## ending／state → 後續映射
- `cave_formula_rebuilt OR cave_formula_saved` 且有可核對材料 → 可進入《三份礁洞拓本有一份多出第八行》。
- `cave_formula_lost` 且全部材料永久失去 → 關閉該後傳。
- `eighth_line_exposed`、`eighth_line_contained`、`eighth_line_circulated`：目前均不指定下一份必要後續。

## 多來源條件
目前沒有多來源節點；後傳只直接依賴根任務。

## 維護註記
不得把偽增補升格成正式武學來源；不得改寫根任務角色是否取得武學來源。未來若引用根任務 NPC，須使用其實際 `NPC#前作編號@前作劇名` 並讀取該桌狀態。目錄只作關係索引，不搬動或複製劇本檔。
