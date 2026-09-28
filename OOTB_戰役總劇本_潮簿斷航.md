# 戰役總劇本：潮簿斷航

- `campaign_id`: `ootb-campaign-tide-ledger-broken-route`
- 版本：1.1.0
- 狀態：已完結
- 已正式完成階段：`ootb-campaign-tide-ledger-broken-route-01` 至 `-04`
- 正式檔：`OOTB_戰役任務_潮簿斷航(01)_鹽棧三本潮簿有一本總在封倉後多一頁.md`、`(02)_兩艘驗潮艇有一艘總在換旗後少一名槳手.md`、`(03)_舊船塢七枚銅釘有一枚總在夜潮前換了頭.md`、`(04)_定潮島外四道燈號有一道總在風停後才亮.md`
- 地點：承泰二十一年，西海道海陵外港、蒼龍灣、定潮島外航道
- 等級走向：6–8、7–10、9–12、11–14
- repository 總綱版本只定義作者權威；單桌實際姓名、例外狀態與已裁定承接只存在該桌 `campaign_save`

## 跨篇核心答案與既存因果
海陵一個地方船料承包網長期利用報廢、補領與潮損名義轉售仍可用船料與器件。帳物差額擴大後，帳房策劃利用驗潮艇交班與錯誤燈號替付費船隻製造短暫無核驗窗口，同時令正常商船延誤以增加可抽取費用。這是地方承包網與少數被收買人員的局部犯罪，不代表海關、水師、船盟或任何門派共同政策。

戰役開始前，偷換船料、雙層帳與收買艇班均已成立；假燈器件尚未全部取得。若玩家不介入，帳房會在十至十四日內取得器件，在濃霧夜試行假燈序，使一艘正常商船接近淺礁。玩家介入後的轉運時間、人手與器材只按下列 state 反應，不鎖成固定劇情。

## 跨篇真實時間線
1. 數月前：承包網開始把仍可用船料列作潮損報廢再轉售。
2. 三旬前：帳房發現單靠報廢帳不足以遮掩差額，開始收買驗潮艇領班。
3. 七日前：鹽貨延誤引發貨主複核；棧吏補頁遮掩最新一批差額。
4. 戰役開始：第一階段由補頁異常進入。
5. 若查核威脅帳鏈：帳房提前使用艇班窗口移器件，形成第二階段。
6. 若艇班窗口暴露或器件被追：承包網搶在船塢查核前取得舊燈號器件，形成第三階段。
7. 只有第三階段正式留下可承接接口時，濃霧窗口與既有假燈計畫形成末篇；若此前接口永久失去，戰役在相應 ending 提早收束。

## 跨篇主要行動者
### `actor_ledger`／`NPC#1@戰役:潮簿斷航`
地方船料承包網帳房與策劃者；姓名欄 `姓?-名?`；首次規劃／正式登場：01。知道雙層帳、付款鏈與假燈計畫；不知道玩家實際掌握多少證據。利益是保住長期抽成並避免被正式查核。資源為帳冊、憑證、賄款、跑腿與既有付款；限制是沒有正式港務權力。`ledger_chain=proven` 或 `harbor_alert=raised|lockdown` 時停用原憑證、分拆付款並提前轉器件；被拘留／死亡後只剩已付款舊指令，不產生新策劃。

### `actor_boat`／`NPC#2@戰役:潮簿斷航`
驗潮艇領班；姓名欄 `姓?-名?`；首次規劃：01，正式登場：02。因私人債務收錢安排交班漏洞；知道付款者與轉運，不知道完整假燈用途。利益是清債並保住資格。若確認計畫會危及正常船且有可信出路，可倒戈；倒戈後帳房停用原艇班。

### `actor_yard`／`NPC#3@戰役:潮簿斷航`
船塢工頭；姓名欄 `姓?-名?`；首次規劃：01，正式登場：03。參與偷換船料，後來發現燈號用途會危及正常船，開始留雙槽銅釘與拓片暗記自保。利益由保住收入轉為避免人命並保全自證材料；有可信合法出路時合作。

### `actor_runner`／`NPC#4@戰役:潮簿斷航`
跑腿頭目；姓名欄 `姓?-名?`；首次規劃／正式登場：01。知道交付地點、暗號與器件轉移，不懂完整帳法。利益是收尾款且不替帳房頂罪；付款中斷或被切割時手下容易散去。拘留／死亡／散去後，只有已付款短工可完成一次既定搬運。

### `actor_harbor`
地方港務查核制度 actor，沒有單一 NPC 實體。初始只見零散事故；利益是維持航道與帳物可核對；有查簿、扣貨及暫停承包憑證權限，但需可核對證據。`harbor_alert` 升高時縮短犯罪方可用窗口並增加合法支援。

## 戰役級 NPC registry
- `NPC#1@戰役:潮簿斷航`：`姓?-名?`；`actor_ledger`；承包網帳房；首次規劃／正式登場01。
- `NPC#2@戰役:潮簿斷航`：`姓?-名?`；`actor_boat`；驗潮艇領班；首次規劃01、正式登場02。
- `NPC#3@戰役:潮簿斷航`：`姓?-名?`；`actor_yard`；船塢工頭；首次規劃01、正式登場03。
- `NPC#4@戰役:潮簿斷航`：`姓?-名?`；`actor_runner`；跑腿頭目；首次規劃／正式登場01。
以上編號永久保留，不因死亡、退出或篇章結果重用。各階段本地 NPC 不升格為跨篇人物。

## Campaign state
`ledger_chain`: unknown | suspected | proven
`boat_window`: intact | disrupted | exposed
`yard_marks`: unknown | secured | destroyed
`signal_kit`: not_acquired | partial | acquired | seized | destroyed
`actor_ledger_status`: free | watched | detained | escaped | dead
`actor_boat_status`: active | defected | detained | escaped | dead
`actor_yard_status`: active | cooperating | detained | escaped | dead
`actor_runner_status`: active | scattered | detained | escaped | dead
`harbor_alert`: low | raised | lockdown
`public_attribution`: none | contractor_network | broad_harbor_blame
`campaign_status`: active | partly_completed | failed | completed
`campaign_progress`: 已結算階段數/4

## 01：鹽棧三本潮簿有一本總在封倉後多一頁
無前置；6–8級，小型。因貨主複核發現封倉後補頁而介入。局部真相：棧吏收錢補頁遮掩被列潮損的可用船料，棧吏有責但非策劃者。輸入：共同基準。直接使用 `NPC#1`、`NPC#4`。輸出主要改變 `ledger_chain`、`harbor_alert`。
- `TL01_E01` 帳鏈坐實：`ledger_chain=proven, harbor_alert=raised`；可承接02；`active,1/4`。
- `TL01_E02` 疑點留下：`ledger_chain=suspected`；帳房兩日內利用艇班轉器件；可承接02；`active,1/4`。
- `TL01_E03` 局部結案：共同鏈接口永久失去；`partly_completed,1/4`。玩家可見收束：貨主追回本批損失，鹽棧換掉有責人員；數日後港邊仍有交班延誤抱怨，但角色沒有可靠證據連回本案。
- `TL01_E04` 放棄：`failed,1/4`。

## 02：兩艘驗潮艇有一艘總在換旗後少一名槳手
7–10級，中型。解鎖：`TL01_E01 OR TL01_E02` 且前篇已正式裁定可承接。因查核風險令帳房提前使用艇班空位轉器件；玩家由前篇簽押、貨物流向或帳鏈介入。直接使用 `NPC#1`、`NPC#2`、視 state 使用 `NPC#4`。輸入 `ledger_chain/harbor_alert` 及 actor 狀態；輸出 `boat_window/signal_kit/actor_boat_status`。
- `TL02_E01`：窗口封住；`boat_window=exposed`，且領班倒戈或 `ledger_chain=proven`；可承接03；`active,2/4`。
- `TL02_E02`：`boat_window=disrupted, signal_kit=partial`；船塢方向成立；可承接03；`active,2/4`。
- `TL02_E03`：本夜違規已止但所有船塢來源永久失去；`partly_completed,2/4`。玩家可見收束：水道恢復正常、艇班撤換；角色知道有人利用交班漏洞，卻沒有可靠方向再追。
- `TL02_E04` 放棄：`failed,2/4`。

## 03：舊船塢七枚銅釘有一枚總在夜潮前換了頭
9–12級，中型。解鎖：第二階段已裁定可承接，且 `(TL02_E01 AND (actor_boat_status=defected OR ledger_chain=proven)) OR TL02_E02`。工頭暗記與器件批號形成新追痕；玩家由器件、口供或帳鏈介入。直接使用 `NPC#1`、`NPC#3`，視 state 使用 `NPC#4`。輸入前述 actor、`signal_kit/boat_window`；輸出 `yard_marks/signal_kit`。
- `TL03_E01`：`signal_kit=seized|destroyed` 且假燈目的確認；可承接04，敵方只剩粗糙替代器材；`active,3/4`。
- `TL03_E02`：`signal_kit=partial|acquired` 且備用燈序確認；可承接04；`active,3/4`。
- `TL03_E03`：船塢侵吞已處理但所有出航接口永久失去；`partly_completed,3/4`。玩家可見收束：船塢恢復查驗，涉事物料逐件清點；海面仍偶有錯燈傳聞，卻沒有足以出航追查的可靠線索。
- `TL03_E04` 放棄：`failed,3/4`。

## 04：定潮島外四道燈號有一道總在風停後才亮
11–14級，大型。解鎖：03已裁定可承接且 `TL03_E01 OR TL03_E02`。輸入此前全部仍有效 state；直接使用仍可行動的戰役 NPC。濃霧窗口使既有假燈計畫進入最後一次執行；state 只改敵方資源、港務支援、證據路線與開場，不重算承接。
- `TL04_E01` 航道守住、責任坐實：`completed,4/4`。
- `TL04_E02` 航道守住、主責逸走：逃犯為持續後果；`completed,4/4`。
- `TL04_E03` 代價止航：已合理建立船貨／人員損失但後續假燈停止；`completed,4/4`。
- `TL04_E04` 假燈得逞：核心阻止目標失敗，但原定末篇正式跑完；`completed,4/4`。
- `TL04_E05` 放棄：`failed,4/4`。

## 條件式反應
- `ledger_chain=proven`：帳房停用原憑證、分拆付款。
- `harbor_alert=raised|lockdown`：艇班縮短或放棄原窗口，改腳船／假簽到。
- `actor_boat_status=defected`：帳房停止原艇班付款；倒戈口供提供來源但不自動證明全部帳鏈。
- `yard_marks=secured`：暗記可對照器件來源。
- `signal_kit=seized|destroyed`：只剩臨時遮板、腳船燈及既知備用序列，操作距離更近。
- `actor_ledger_status=detained|dead`：只執行已付款、已明確交代的一次舊指令。
- `actor_runner_status=scattered|detained|dead`：只能用已付款短工或縮小轉運，不繼承跑腿頭目資訊。

## 跨篇韌性與收束邊界
任何戰役 NPC 都不保證活到末篇。死亡、拘留、倒戈、逃走及永久傷勢寫入 `campaign_save`；後篇按 state 縮小能力。關鍵證據均有不同因果來源；來源被毀提高成本或降低可處置程度，不憑空再生。每個非末篇 ending 已明確分類可承接或提早戰役結局；實際桌次只在結算時裁定一次承接。

末篇後，逃犯、私人債務、受損商船與港務改革只保存為世界後果，不自動建立第五篇。