# 戰役總劇本：潮簿斷航

- campaign_id: `ootb-campaign-tide-ledger-broken-route`
- 版本：1.0.0
- 狀態：規劃中
- 已發布階段：無
- 規劃階段：4
- 地點：承泰二十一年，西海道海陵外港、蒼龍灣、定潮島外航道。
- 等級走向：6–8、7–10、9–12、11–14。

## 跨篇核心答案
海陵一個地方船料承包網長期利用報廢、補領與潮損名義轉售仍可用船料與器件。帳物差額擴大後，帳房策劃利用驗潮艇交班與錯誤燈號替付費船隻製造短暫無核驗窗口，同時令正常商船延誤以增加可抽取費用。這是地方承包網與少數被收買人員的局部犯罪，不代表海關、水師、船盟或蒼龍門的共同政策。

戰役開始時，他們已能操縱外港小段流程，尚未控制定潮島主航道。下一步是取得舊式燈號器件及備用燈序，在濃霧夜試行假燈號。若玩家不介入，約十至十四日內會出現一次足以令正常商船接近淺礁的錯誤引導。

## 主要行動者
- `actor_ledger`／`NPC#1@戰役:潮簿斷航`：承包網帳房與策劃者。知道雙層帳、付款與假燈號計畫；資源是帳冊、供料憑證、賄款與跑腿；沒有正式港務權力。被查時先補帳、轉移器件，再切割被收買人員。
- `actor_boat`／`NPC#2@戰役:潮簿斷航`：驗潮艇領班。為私人債務收錢安排交班漏洞；知道付款者但只知假燈號部分內容。若確認計畫會危及正常船，可倒戈。
- `actor_yard`／`NPC#3@戰役:潮簿斷航`：船塢工頭。參與偷換船料，得知燈號用途後開始留私人暗記自保；願在有可信出路時合作。
- `actor_runner`／`NPC#4@戰役:潮簿斷航`：跑腿頭目。知道交付地點、暗號與器件轉移，不知道完整帳法；付款中斷後手下容易散去。
- `actor_harbor`：地方港務查核制度 actor，無單一 NPC key。只見零散事故；有查簿、扣貨及暫停承包憑證權限，但需要可核對證據。

戰役 NPC 編號永久保留。後續如新增跨篇具體人物，先更新本總綱 registry、接口與版本。

## Campaign state
- `ledger_chain`: unknown | suspected | proven
- `boat_window`: intact | disrupted | exposed
- `yard_marks`: unknown | secured | destroyed
- `signal_kit`: not_acquired | partial | acquired | seized | destroyed
- `actor_ledger_status`: free | watched | detained | escaped | dead
- `actor_boat_status`: active | defected | detained | escaped | dead
- `actor_yard_status`: active | cooperating | detained | escaped | dead
- `actor_runner_status`: active | scattered | detained | escaped | dead
- `harbor_alert`: low | raised | lockdown
- `public_attribution`: none | contractor_network | broad_harbor_blame
- `campaign_status`: active | partly_completed | failed | completed
- `campaign_progress`: 已結算階段數/4

## 第一階段：鹽棧三本潮簿有一本總在封倉後多一頁
建議 6–8 級，小型。無前置。七日前鹽貨延誤令貨主要求複核；補抄頁與原潮簿用印時點不合。玩家受委託查明帳務異常與損失。局部真相是帳房指示棧吏補抄以遮掩被列作潮損的可用物料；棧吏有責但非策劃者。

- `TL01_E01` 帳鏈坐實：`ledger_chain=proven, harbor_alert=raised`；可承接第二階段；`active, 1/4`。
- `TL01_E02` 疑點留下：`ledger_chain=suspected`；策劃者兩日內利用驗潮艇轉移器件；可承接；`active, 1/4`。
- `TL01_E03` 局部結案：本批事件完整處理但無可靠共同鏈接口；提早收束，`partly_completed, 1/4`。玩家可見：貨主追回本批損失，鹽棧換掉有責人員；數日後港邊仍有交班延誤抱怨，角色手中沒有足以連回本案的證據。
- `TL01_E04` 放棄：提早收束，`failed, 1/4`。

## 第二階段：兩艘驗潮艇有一艘總在換旗後少一名槳手
建議 7–10 級，中型。解鎖：`TL01_E01 OR TL01_E02`，且前篇已裁定可承接。帳房因查核風險提前利用艇班窗口轉移器件；若警戒已升高則縮短窗口。玩家由前篇簽押與新缺員異常介入。局部真相是領班安排假簽到，空出艇位讓跑腿轉運。

- `TL02_E01` 窗口封住：`boat_window=exposed`；若領班倒戈或 `ledger_chain=proven`，可承接第三階段；`active, 2/4`。
- `TL02_E02` 人散貨在：`boat_window=disrupted, signal_kit=partial`；可承接第三階段；`active, 2/4`。
- `TL02_E03` 只止這一夜：本篇違規被阻止，但所有船塢來源永久失去；提早收束，`partly_completed, 2/4`。玩家可見：當夜水道恢復正常，涉事艇班被撤換；角色知道有人利用交班漏洞，卻沒有可靠方向再追。
- `TL02_E04` 放棄：`failed, 2/4`。

## 第三階段：舊船塢七枚銅釘有一枚總在夜潮前換了頭
建議 9–12 級，中型。解鎖：第二階段已裁定可承接，且 `(TL02_E01 AND (actor_boat_status=defected OR ledger_chain=proven)) OR TL02_E02`。承包網要在查核收緊前取得舊燈號器件；船塢工頭的私人暗記形成可追痕跡。玩家由器件、口供或帳鏈指向同一批號。

- `TL03_E01` 器件扣下：`signal_kit=seized|destroyed` 且假燈號目的已確認；第四階段仍可承接，但犯罪方只能用較粗糙替代器材；`active, 3/4`。
- `TL03_E02` 只追回一半：`signal_kit=partial|acquired` 且已確認定潮島外備用燈序；可承接；`active, 3/4`。
- `TL03_E03` 船塢止損：侵吞被處理但所有下一步接口永久失去；`partly_completed, 3/4`。玩家可見：船塢恢復查驗，涉事物料逐件清點；海面仍偶有錯燈傳聞，卻沒有足以出航追查的可靠線索。
- `TL03_E04` 放棄：`failed, 3/4`。

## 第四階段：定潮島外四道燈號有一道總在風停後才亮
建議 11–14 級，大型。解鎖：第三階段已裁定可承接，且 `TL03_E01 OR TL03_E02`。開局讀取此前全部仍有作用的 state；這些 state 只改變敵方資源、港務支援、證據路線與開場，不重算已裁定承接。濃霧窗口到來，仍自由且有資源的行動者嘗試最後一次假燈序；已拘留或死亡者不會被強制回場。

- `TL04_E01` 航道守住、責任坐實：`completed, 4/4`。
- `TL04_E02` 航道守住、主責逸走：末篇正式收束；逃犯成持續後果，`completed, 4/4`。
- `TL04_E03` 代價止航：阻止後續假燈號但已有合理建立的船貨或人員損失；`completed, 4/4`。
- `TL04_E04` 假燈得逞：核心阻止目標失敗，按本篇已建立風險結算；戰役失敗性收束但原定末篇已完成，`completed, 4/4`。
- `TL04_E05` 末篇放棄：`failed, 4/4`。

## 條件式反應
- `ledger_chain=proven`：帳房停用原憑證、分拆付款；後篇改由多筆小額時間關聯追查。
- `harbor_alert=raised|lockdown`：艇班縮短或放棄原窗口，轉用腳船／假簽到。
- `actor_boat_status=defected`：帳房停止原艇班付款並催取器件；倒戈口供提供來源但不自動證明全部帳鏈。
- `yard_marks=secured`：工頭可用暗記對照器件來源。
- `signal_kit=seized|destroyed`：犯罪方只能用臨時遮板、腳船燈及已知備用序列，需更近距離操作，增加暴露途徑。
- `actor_ledger_status=detained|dead`：跑腿只執行已付款、已明確交代的一次舊指令；不自動繼承策劃能力。
- `actor_runner_status=scattered|detained|dead`：帳房須臨時找短工或縮小轉運，留下新目擊來源。

## 跨篇韌性與收束邊界
任何戰役 NPC 都不保證活到末篇。死亡、拘留、倒戈、失蹤及永久傷勢寫入 `campaign_save`，後篇按 state 縮小能力或使用已存在的替代行動鏈。關鍵證據均有不同因果來源；來源被毀會提高成本或降低可處置程度，不會憑空再生。玩家若提前公開充分證據，港務可升級查核並令某階段自然提早收束；不得強迫四篇全跑。

本戰役只回答海陵外港這條承包、驗潮、船塢與燈號犯罪鏈如何運作及如何收束。末篇後即使仍有逃犯、私人債務、受損商船或港務改革，也只保存為持續世界後果，不自動建立第五篇。
