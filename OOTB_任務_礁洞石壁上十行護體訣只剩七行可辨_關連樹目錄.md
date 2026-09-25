# 《礁洞石壁上十行護體訣只剩七行可辨》關連樹目錄

- 根任務：《礁洞石壁上十行護體訣只剩七行可辨》
- 根 `script_id`：`ootb_martial_canglong_cave_20260924`

## 樹內節點
| 劇名 | 檔名／script_id | 直接來源 | 關連類型 | 必要前置 |
|---|---|---|---|---|
| 《礁洞石壁上十行護體訣只剩七行可辨》 | `OOTB_任務_礁洞石壁上十行護體訣只剩七行可辨.md`／`ootb_martial_canglong_cave_20260924` | 無 | 根任務 | 無 |
| 《三份礁洞拓本有一份多出第八行》 | `OOTB_任務_三份礁洞拓本有一份多出第八行.md`／`ootb_related_cave_eighth_line_20260924` | 根任務 | 後傳 | `cave_formula_rebuilt OR cave_formula_saved`，且仍有可核對七行材料 |
| 《四張退貨單有一張蓋著舊礁印》 | `OOTB_任務_四張退貨單有一張蓋著舊礁印.md`／`ootb_related_cave_return_slip_20260925` | 《三份礁洞拓本有一份多出第八行》 | 後傳 | `eighth_line_exposed OR eighth_line_contained OR eighth_line_circulated` |

## 關連圖
`根:cave_formula_rebuilt OR cave_formula_saved → 三份礁洞拓本有一份多出第八行`

`三份礁洞拓本有一份多出第八行:(eighth_line_exposed OR eighth_line_contained OR eighth_line_circulated) → 四張退貨單有一張蓋著舊礁印`

`cave_formula_lost` 且全部可核對材料永久失去時，第一份後傳不可達，因此後續舊礁印節點亦不可達。

## 共同背景基線
礁洞材料的可驗證內容只支持【龍鱗護體神功】至10級的有限門派外來源；不帶 `[來自蒼龍門]`，不提供蒼龍門身份、引薦或11級以上來源。石壁、拓本與角色實際取得狀態依根任務結算保存。後傳中的「第八行」與「舊礁印」均不改寫此共同背景，也不得自行成為新的武學來源。

## branch-specific state
- `cave_formula_rebuilt`：至少一份完整七行拓本保全；合資格角色可能各自建立至10級來源。
- `cave_formula_saved`：石壁或拓片被保全，未建立武學來源。
- `cave_formula_lost`：若全部可核對材料永久失去，第一份後傳不可開始。
- `eighth_line_exposed`：假第八行被完整辨偽並阻止交割；後作可取得公開辨偽記錄。
- `eighth_line_contained`：假本被扣但未完全定責；後作只可取得封存收據。
- `eighth_line_circulated`：假本完成交割；後作可取得交易貨單副記。

## 可累積 state
根任務中角色個別是否已建立【龍鱗護體神功】來源，可與任何後傳 ending 同時存在；後傳不得改寫其他角色的既有來源。舊礁印節點只處理來源鏈與退貨文書，不改變根任務的武學來源資格。

## 互斥 state
`cave_formula_rebuilt`、`cave_formula_saved`、`cave_formula_lost` 作為根任務 ending 互斥。`eighth_line_exposed`、`eighth_line_contained`、`eighth_line_circulated` 三者互斥。`old_reef_seal_broken`、`old_reef_seal_held`、`old_reef_seal_sailed` 三者互斥。

## ending／state → 後續映射
- `cave_formula_rebuilt OR cave_formula_saved` 且有可核對材料 → 可進入《三份礁洞拓本有一份多出第八行》。
- `cave_formula_lost` 且全部材料永久失去 → 關閉第一份及其後續節點。
- `eighth_line_exposed OR eighth_line_contained OR eighth_line_circulated` → 可進入《四張退貨單有一張蓋著舊礁印》；三條branch只改變開場可用文書，不改變舊礁印的客觀來源。
- `old_reef_seal_broken`、`old_reef_seal_held`、`old_reef_seal_sailed`：目前均不指定下一份必要後續。

## 多來源條件
目前沒有多來源節點；每個後傳只直接依賴上一個節點。不得把根任務僅作背景資料的存在誤列為舊礁印節點的第二條直接來源。

## 維護註記
不得把偽增補或舊礁印升格成正式武學來源；不得改寫根任務角色是否取得武學來源。未來若引用既有劇本 NPC，須使用其實際 `NPC#前作編號@前作劇名` 並讀取該桌狀態。目錄只作關係索引，不搬動或複製劇本檔。