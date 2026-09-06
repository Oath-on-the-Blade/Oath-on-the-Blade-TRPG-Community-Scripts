# OOTB 戰役總劇本：寒江三印

## 規格頭
- 戰役名：寒江三印
- `campaign_id`：`OOTB-CAMPAIGN-HANJIANG-SANYIN-001`
- 總劇本版本：1.1
- 戰役狀態：已完結
- 已正式完成的階段劇本：
  1. `OOTB_戰役任務_寒江三印(01)_白水埠的半枚驗印.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-01`
  2. `OOTB_戰役任務_寒江三印(02)_石梁倉的兩次入簿.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-02`
  3. `OOTB_戰役任務_寒江三印(03)_青篙渡沒有登記的夜船.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-03`
  4. `OOTB_戰役任務_寒江三印(04)_舊堰道的第三方印記.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-04`
- 當前規劃中的下一階段：無；本戰役作者層共四階段
- 戰役共同起點：昊曆二百四十一年，承泰二十一年；江南道北緣白水埠及寒江沿線
- 主要地理範圍：江南道境內寒江支流、白水埠、石梁倉、青篙渡、白蘆岔與舊堰道。以上均為本戰役局部新增地點，不改寫 Handbook 固定城市、山川與十道邊界
- 等級／規模走向：第一階段 6–9 級／R8／中型；第二階段 7–10 級／R9／中型；第三階段 8–11 級／R10／大型；第四階段 9–12 級／R11／大型
- 共用權威：Handbook `世界知識庫/`、`內容庫/`、`劇本設計規則/` 當前共同基準
- repository 總劇本與桌次狀態：本檔只保存作者權威的跨篇真相、actor、NPC registry、state、ending 承接分類與階段解鎖路線；單桌實際姓名、ending、例外狀態與 current `campaign_status` 寫入 `campaign_save`，不回寫為共用正典

## 一、跨篇核心答案
寒江沿線近兩月出現驗貨木牌重號、官倉短斤與上游舊驗記反覆出現等異常。三種異常源於同一套被拆開使用的承攬接口：同批高價修堰鐵件能在不同制度段落取得表面上彼此獨立的認列，再利用換包、換車與夜運離開正規流向。

承攬管事 `<NPC#1@戰役:寒江三印: 姓?-名?>` 掌握三段接口，最初為填補墊款缺口挪用一批鐵件，之後為補平前一批帳目而擴大套轉。白水埠驗牌手 `<NPC#2@戰役:寒江三印: 姓?-名?>` 只知道自己曾按要求補刻舊號；石梁倉副管 `<NPC#3@戰役:寒江三印: 姓?-名?>` 知道短斤且收錢改過入倉時辰，但不知道完整末路；夜船船戶 `<NPC#4@戰役:寒江三印: 姓?-名?>` 知道自己收錢運官修鐵件與接貨路線，但不知道倉簿如何閉合。

真正受益與維持接口者集中在 `<NPC#1>` 及其交易對手；執行層不是人人知情。本戰役的核心不是把所有局部責任者改寫成無責，而是分清每一段的實際行為、認知與責任，再判定能否以可交付來源把三段合成同一承攬流程。

### 已成立與尚未發生
- 戰役開始前：同類流程已至少運作數次；`<NPC#2>` 補刻過重號舊牌；`<NPC#3>` 已改過時辰；`<NPC#4>` 已跑過夜運
- 戰役開始時尚未固定的未來：簿束是否焚毀、最後貨物是否被截、各 NPC 是否逃走／合作／被拘／死亡；全部依階段 state 與玩家行動推進
- 後篇不得為了原定劇情把前篇已正式固定的人物／證物狀態重置

## 二、跨篇真實時間線
1. 約兩月前：`<NPC#1>` 因承攬墊款緊張第一次挪出已報進埠的鐵件，原想以下批補回。
2. 約七週前：為使帳面接口可繼續運作，要求 `<NPC#2>` 以「舊牌磨損」理由補刻同號驗牌。
3. 約六週前：石梁倉首次短斤；`<NPC#3>` 收錢後改記時辰。
4. 約一月前：`<NPC#4>` 接第一趟不進正渡簿的夜運。
5. 約三週前：第二輪套轉完成；執行層開始各自留下自保或程序痕跡。
6. 約十日前：官倉已看到總重與料單不合，但尚未建立跨段因果。
7. 戰役開始前三日：白水埠發現可與舊牌相合的半枚斷裂驗印，形成第一階段異常。
8. 戰役開始時：`<NPC#1>` 知道總核逼近，準備清理最後一批貨與能串段的文書。

### 不介入基準與條件式反應
- 低警覺：仍優先索回物證、買通局部知情者並維持原路。
- `contractor_alert=raised`：停止新增重號牌，搬移部分簿頁並調整裝車時段。
- `contractor_alert=high`：不再補帳，優先移動／焚毀簿束、取消原夜船接頭、視 `final_cargo_status` 棄貨或移貨。
- 階段正文的具體時鐘優先於此總綱概述；前篇 ending 可提前、取消或改變上述行動。

## 三、跨篇主要行動者
### `actor_contractor` — `<NPC#1@戰役:寒江三印: 姓?-名?>`
- 身份：地方修堰承攬管事，可接觸進埠、入倉、夜運與工棚交貨接口，但不直接控制官署
- 初始知道：完整三段流程、各批數量、改道路線與哪些人只知局部
- 不知道：玩家何時取得哪一份未公開證據
- 核心利益：避免破產／刑責並保命；證據無法回收時傾向用有限合作換正式處理
- 資源：承攬工人、合法料車、舊堰工棚、少量現銀與流程知識；沒有無限武力
- 反應：讀取 `contractor_alert`、`warehouse_copy_secured`、`boatman_cooperating`、`final_cargo_status`；高警覺時移簿、改路，若核心已可交付則可合作

### `actor_seal_clerk` — `<NPC#2@戰役:寒江三印: 姓?-名?>`
- 身份：白水埠驗牌手
- 知道：自己補刻過舊號，後來發現重號異常；不知道短斤與夜運全貌
- 核心利益：保工作並避免被寫成完整主謀
- 反應：可信保護＋獨立證據可合作；私刑／公開定罪壓力可令其逃；後篇只按 `seal_clerk_status` 與已保存證物使用

### `actor_warehouse` — `<NPC#3@戰役:寒江三印: 姓?-名?>`
- 身份：石梁倉副管
- 知道：短斤、改時辰、收賄與貨物大致離倉方向；不知道完整買方與三段全貌
- 核心利益：避免成為唯一替罪者，同時承擔自己確有的收賄責任
- 資源：倉簿接觸權、自保私抄與流程知識
- 反應：獨立矛盾足夠時可合作；死亡／逃亡／被拘後只使用存檔實值，不重置

### `actor_boatman` — `<NPC#4@戰役:寒江三印: 姓?-名?>`
- 身份：青篙渡短駁船戶
- 知道：側靠、接貨、改道路線；不知道倉簿全貌與最終買方身份
- 核心利益：保船、保船員、不替承攬方承擔超出實際所知的責任
- 反應：船員安全與有限責任被承認時可合作；受攻擊時先撤；後篇只按 `boatman_cooperating` 與實際保存來源使用

### `actor_buyer`
- 身份：數名短期收購工料的私人交易人，沒有單一具名組織身份
- 知道：貨有官修背景且來路不乾淨；不知道完整三段流程
- 核心利益：低價收貨並避開官案
- 邊界：不建立新相對名譽對象，不替 `<NPC#1>` 無限提供人手

## 四、戰役級 NPC 佔位符權威列表
| Key | 姓名欄 | 身份／跨篇功能 | actor_key | 首次正式登場／script_id | alias |
|---|---|---|---|---|---|
| `NPC#1@戰役:寒江三印` | `姓?-名?` | 承攬管事；跨篇主要責任接口 | `actor_contractor` | 第一階段／`OOTB-CAMPAIGN-HANJIANG-SANYIN-01` | 無 |
| `NPC#2@戰役:寒江三印` | `姓?-名?` | 白水埠驗牌手 | `actor_seal_clerk` | 第一階段／`OOTB-CAMPAIGN-HANJIANG-SANYIN-01` | 無 |
| `NPC#3@戰役:寒江三印` | `姓?-名?` | 石梁倉副管 | `actor_warehouse` | 第二階段／`OOTB-CAMPAIGN-HANJIANG-SANYIN-02` | 無 |
| `NPC#4@戰役:寒江三印` | `姓?-名?` | 青篙渡夜船船戶 | `actor_boatman` | 第三階段／`OOTB-CAMPAIGN-HANJIANG-SANYIN-03` | 無 |

編號1–4永久分配；本戰役已完結，不再在現有四篇內新增跨篇 NPC。

## 五、Campaign State Registry
| state | 型別／值 | 初始值 | 建立／修改來源 | 後篇用途 |
|---|---|---|---|---|
| `seal_link_exposed` | bool | false | 第一階段 | 重號舊牌接口是否已可靠建立 |
| `seal_clerk_status` | `free/cooperating/fled/detained/dead` | `free` | 第一階段 | 驗牌手是否可再作證／辨識 |
| `old_tag_secured` | bool | false | 第一階段 | 是否保存舊牌直接物證 |
| `contractor_alert` | `low/raised/high` | `low` | 各階段 | 承攬管事反應強度；不得無因降低 |
| `warehouse_copy_secured` | bool | false | 第二階段 | 副管私抄頁是否封存 |
| `warehouse_status` | `free/cooperating/fled/detained/dead` | `free` | 第二階段 | 副管持續狀態 |
| `night_route_known` | bool | false | 第二／三階段 | 是否已有青篙渡夜運接口 |
| `boatman_cooperating` | bool | false | 第三階段 | 船戶是否正式合作 |
| `buyer_point_known` | bool | false | 第三階段 | 是否掌握末端接頭／替代接點，可直接作末篇接口 |
| `ledger_bundle_status` | `intact/moved/burned/secured` | `intact` | 第三／四階段 | 流水簿束物理狀態 |
| `final_cargo_status` | `pending/diverted/seized/destroyed` | `pending` | 第三／四階段 | 最後一批鐵件狀態；由船帶離但仍沿非正規路移動記 `diverted`，不另造 `escaped` 同義值 |
| `contractor_status` | `active/fled/detained/dead/cooperating` | `active` | 第四階段及可預見例外 | 主要責任者最終狀態 |
| `three_links_proven` | bool | false | 第四階段 | 是否以可交付來源把舊標、倉時、夜批三段與承攬責任合成同一核心鏈 |

單篇傷勢、普通消耗、臨時位置及「哪一份具體替代來源已保存」依階段 ending 與桌次 `campaign_save` 保存；它們不是新的平行 campaign state。

## 六、階段接口
### 第一階段〈白水埠的半枚驗印〉
- 狀態：正式完成
- 檔名／ID：`OOTB_戰役任務_寒江三印(01)_白水埠的半枚驗印.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-01`
- 輸入：初始 state
- 直接使用：`NPC#1`、`NPC#2`
- 局部目標：查明斷印／舊牌異常、處理驗牌手與證物
- 主要輸出：`seal_link_exposed`、`seal_clerk_status`、`old_tag_secured`、`contractor_alert`
- `HJ01-E1`：可承接第二階段；`campaign_status=active`
- `HJ01-E2`：可承接第二階段；`campaign_status=active`，第二篇先建立較弱入口的第二個矛盾
- `HJ01-E3`：不可承接；`partly_completed`；玩家可見收束〈斷口留在水裡〉
- `HJ01-E4`：任務放棄；`failed`；玩家可見收束〈埠房關門〉
- 承接裁決在第一階段正式結算時一次寫入 `campaign_save`，下一篇不重算

### 第二階段〈石梁倉的兩次入簿〉
- 狀態：正式完成
- 檔名／ID：`OOTB_戰役任務_寒江三印(02)_石梁倉的兩次入簿.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-02`
- 解鎖：`(HJ01-E1 OR HJ01-E2) AND campaign_status=active`
- 讀取：第一階段全部仍有效 state，尤其 `seal_link_exposed/old_tag_secured/seal_clerk_status/contractor_alert`
- 直接使用：`NPC#3`；按 state 引用 `NPC#1/#2`
- 局部目標：重建兩次入簿、短斤與倉外換車，處理副管責任並找離倉方向
- 輸出：`warehouse_copy_secured`、`warehouse_status`、`night_route_known`、`contractor_alert`
- `HJ02-E1`：私抄頁＋另一去向來源；`night_route_known=true`；`active`；可承接第三階段
- `HJ02-E2`：私抄頁失去但兩個獨立去向來源成立；`night_route_known=true`；`active`；可承接第三階段
- `HJ02-E3`：倉內責任成立但全部去向來源永久失去；`night_route_known=false`；`partly_completed`；收束〈倉門內的一筆罪〉
- `HJ02-E4`：任務放棄；`failed`；收束〈帳頁合上〉
- 承接裁決在第二階段正式結算時一次寫入 `campaign_save`

### 第三階段〈青篙渡沒有登記的夜船〉
- 狀態：正式完成
- 檔名／ID：`OOTB_戰役任務_寒江三印(03)_青篙渡沒有登記的夜船.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-03`
- 解鎖：`(HJ02-E1 OR HJ02-E2) AND night_route_known=true AND campaign_status=active`
- 讀取：第一、二階段仍有效 state；不同 `warehouse_copy_secured/warehouse_status` 改變文件強度而不重置人物
- 直接使用：`NPC#4`；按 state 引用 `NPC#1/#2/#3`
- 局部目標：重建夜船避簿機制、確認同批貨、處理船戶與舊堰末路
- 輸出：`boatman_cooperating`、`buyer_point_known`、`ledger_bundle_status`、`final_cargo_status`、`contractor_alert`
- `HJ03-E1`：船戶合作＋實物末路；`buyer_point_known=true`、`ledger_bundle_status=moved`；`active`；可承接第四階段
- `HJ03-E2`：船戶不合作／失去，但兩個獨立末路來源成立；`ledger_bundle_status=moved`；`active`；可承接第四階段
- `HJ03-E3`：貨物受控但所有末路來源永久失去；`partly_completed`；收束〈一船鐵停在岸上〉
- `HJ03-E4`：任務放棄；`failed`；收束〈夜潮帶走船燈〉
- 承接裁決在第三階段正式結算時一次寫入 `campaign_save`

### 第四階段〈舊堰道的第三方印記〉
- 狀態：正式完成／末篇
- 檔名／ID：`OOTB_戰役任務_寒江三印(04)_舊堰道的第三方印記.md`／`OOTB-CAMPAIGN-HANJIANG-SANYIN-04`
- 解鎖：`(HJ03-E1 OR HJ03-E2) AND campaign_status=active AND (buyer_point_known=true OR ledger_bundle_status=moved OR current final_cargo_status 有第三階段正式保存的舊堰追蹤依據)`
- 讀取：第一至三階段全部仍有效 state 與實際保存的替代證據來源
- 直接使用：`NPC#1`；其他戰役 NPC 只按存檔實值可用
- 局部目標：交叉舊標／倉時／夜批、處理流水簿束、最後貨物與主要承攬責任
- 輸出：`ledger_bundle_status`、`final_cargo_status`、`contractor_status`、`three_links_proven`
- `HJ04-E1`：三段與責任均可交付；`three_links_proven=true`；`campaign_status=completed`
- `HJ04-E2`：完整敏感流水頁毀損，但**舊標、倉時、夜批三段各至少一個**先前保存的可交付來源仍在，且本篇主責有至少兩個獨立來源；`three_links_proven=true`；`completed`
- `HJ04-E3`：只能交付部分核心；`three_links_proven=false`；`partly_completed`；收束〈三枚印只對上兩枚〉
- `HJ04-E4-A`：同一 `HJ04-E4` 的提前撤離變體，結算類型任務放棄；`failed`
- `HJ04-E4-B`：同一 `HJ04-E4` 的責任鏈全失變體，結算類型失敗結局；`failed`；收束〈舊堰只剩灰〉
- 本篇為末篇，不建立下一階段

## 七、跨篇證據與冗餘邊界
- 舊標／重號段：第一階段由斷印／舊牌物理吻合、補刻痕跡、`NPC#2` 有限證詞等來源互證；後篇只使用正式保存者
- 倉時／短斤段：第二階段由正簿矛盾、秤棚副簽、換車坡實物、私抄頁、驛票／腳夫等互證
- 夜批／末路段：第三階段由換班簿、蘆樁／船痕、貨物特徵、改道木片、窄輪短牌／車轍、`NPC#4` 有限證詞互證
- 三段同一流程：第四階段敏感流水頁是強來源；即使燒毀，只有前三段**各至少一個**可交付來源仍在，且本篇建立三記共同流程與 `NPC#1` 責任，才可令 `three_links_proven=true`
- 任一前篇 ending 已把合法接口永久毀掉時，該篇直接提早收束；後篇不補造證據重新接線

## 八、條件式反應矩陣
- `contractor_alert=low`：合法承攬外觀仍在，優先索回物證與局部買通
- `raised`：停新舊牌、移部分簿頁、改裝車時段
- `high`：移／燒簿束、改夜船接點、依貨物實況棄貨／移貨；不再降回毫無戒心
- `seal_clerk_status=cooperating`：只提供其實際知道的刻痕／舊牌技術辨識
- `warehouse_status=cooperating`：只提供倉務流程與已知交款／方向，不替代夜運來源
- `boatman_cooperating=true`：只提供側靠／改道路線，不替代倉務或主責文書
- 任一 NPC `dead/fled/detained`：按已保存物證與狀態運行；不得重生、釋放或回到原位

## 九、主要前篇結果如何改變後篇
- HJ01-E1：第二篇可直接用重號證據展開；E2：先用秤棚等外部矛盾補強入口
- HJ02-E1：第三篇有較強付款／方向文書；E2：依驛票＋腳夫／實物路徑進場
- HJ03-E1：第四篇有船戶合作與改道接口；E2：以簿束搬運／車轍末路進場
- `contractor_alert` 累積，後篇不得重置；前篇 NPC／物件例外以 current `campaign_save` 原樣帶入

## 十、末篇核心處理邊界
第四階段至少可由兩類方法收束：
1. 官署／證據交付：封南口、保簿、交叉三段並控制／說服主要責任者；
2. 實物／動態追截：追車、控火、奪回簿束、用既有來源迫使合作。

單一高 DC、單一死亡或單一自白不能自動證明整個戰役。玩家提前有充分來源可以縮短搜索，但不跳過可交付性；主要責任者死亡時仍只按已保存來源判定。

## 十一、戰役層社會名譽與物質邊界
各階段的俠名、惡名、正式相對名譽、歷練與物質由該篇最終 `.md` 獨立結算；總綱不另加戰役總獎勵、不創造新相對名譽對象。後篇只讀已正式結算、且對人物反應／物理權利有實際意義的結果。

## 十二、作者完成狀態
- 四個正式階段檔均已存在，且各自保存穩定 `script_id`、ending 與 state 寫回規則。
- 本總綱 registry 只含實際使用的四名戰役級 NPC；未新增未登錄跨篇人物。
- `final_cargo_status` 已統一為 `pending/diverted/seized/destroyed`；夜船帶貨離開但仍沿非法路轉移用 `diverted`，不建立 `escaped` 同義 state。
- 非末篇所有 ending 都已分類為「可承接」或「提早戰役結局」；所有任務放棄 ending 均中斷戰役並映射 `failed`。
- 末篇所有正式結果映射到 `completed/partly_completed/failed`，沒有下一篇。
- 作者發布前仍須用本最新總綱＋四篇 final `.md` 通過 `戰役總劇本檢查.md` 與 `戰役整體覆檢.md`；只有覆檢通過後才可整合到 default branch。