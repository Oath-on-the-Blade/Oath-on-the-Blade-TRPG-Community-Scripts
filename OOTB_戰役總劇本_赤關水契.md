# 《赤關水契》戰役總劇本

> OOTB／《武與俠》連續戰役總劇本。本文件是作者層跨篇權威：固定跨篇真相、主要行動者、戰役級 NPC registry、campaign state、六階段接口、解鎖條件、ending 承接分類與條件式反應。單桌實際結果由 `campaign_save` 保存，不回寫本總劇本。

## 戰役規格頭

| 項目 | 內容 |
|---|---|
| 戰役名稱 | 《赤關水契》 |
| campaign_id | `chiguan-water-contract` |
| 總劇本版本 | 1.0.3 |
| 戰役狀態 | 已完結；第1–6階段均已有正式最終劇本檔，並已完成戰役整體覆檢 |
| 已完成階段 | 第1篇《井堡水牌少了第七孔》；第2篇《夜駝隊帶回兩套同號水袋》；第3篇《九折關外埋著一車空陶罐》；第4篇《長風井路一夜多了三座臨時柵》；第5篇《赤關水簿少了四十車》；第6篇《沙海第一場風前的最後一口官井》 |
| 規劃下一階段 | 無；第6篇為正式末篇 |
| 世界起點 | 昊曆241年／承泰21年；隴東道赤關以東至九折關、長風沙海邊緣的官道井堡與商旅補水網 |
| 角色走向 | 第1篇6–9級；第2篇7–10級；第3篇8–11級；第4篇9–12級；第5篇10–13級；第6篇11–14級 |
| 核心類型 | 商旅配水、井堡名額、偽造水牌、夜駝轉運、囤水套利、官面失職、沙海風季前多目標危機 |
| 共用正典 | Handbook `世界知識庫/地理與世界基準/時代與世界基準.md`、`昊國地理.md`；正式相對名譽對象【隴東道民間】【隴東道官府】 |
| 地方新增邊界 | 赤關東驛井堡、石背井堡、灰堰陶場、九折關外二十里轉運坡與地方配水簿均為本戰役局部新增，不建立新的全國官署或固定歷史人物。 |
| 戰役總目標 | 查明合法商旅配水名額如何被重複出售、夜間轉運、藏匿與回填帳目；在第一場大風前切斷可持續套利的條件，同時避免把真正依賴官井生存的商旅與井戶一併斷水。 |

## 正式階段識別

| 序號 | 劇名 | script_id | 檔名 | 狀態 |
|---|---|---|---|---|
| 1 | 井堡水牌少了第七孔 | `ootb-campaign-chiguan-water-1-token-hole-v1` | `OOTB_戰役任務_赤關水契(1)_井堡水牌少了第七孔.md` | 完成 |
| 2 | 夜駝隊帶回兩套同號水袋 | `ootb-campaign-chiguan-water-2-duplicate-skins-v1` | `OOTB_戰役任務_赤關水契(2)_夜駝隊帶回兩套同號水袋.md` | 完成 |
| 3 | 九折關外埋著一車空陶罐 | `ootb-campaign-chiguan-water-3-buried-jars-v1` | `OOTB_戰役任務_赤關水契(3)_九折關外埋著一車空陶罐.md` | 完成 |
| 4 | 長風井路一夜多了三座臨時柵 | `ootb-campaign-chiguan-water-4-three-barriers-v1` | `OOTB_戰役任務_赤關水契(4)_長風井路一夜多了三座臨時柵.md` | 完成 |
| 5 | 赤關水簿少了四十車 | `ootb-campaign-chiguan-water-5-ledger-forty-carts-v1` | `OOTB_戰役任務_赤關水契(5)_赤關水簿少了四十車.md` | 完成 |
| 6 | 沙海第一場風前的最後一口官井 | `ootb-campaign-chiguan-water-6-last-well-v1` | `OOTB_戰役任務_赤關水契(6)_沙海第一場風前的最後一口官井.md` | 完成／末篇 |

# 1. 跨篇核心答案

赤關東出的官道井堡按季節與駝隊規模分配取水時段。真正問題不是「有人偷了一桶水」，而是五個責任層互相利用：

1. 商旅配水掮客 `<NPC#1@戰役:赤關水契: 姓?-名?>`（`ACT-BROKER`）替多支駝隊代辦水牌。他故意把部分合法名額重複出售，再把多出的水引到夜間轉運鏈；他知道會造成白天名額不足，但認為只要每旬補回帳面數量就不會出事。
2. 東驛井簿書吏 `<NPC#2@戰役:赤關水契: 姓?-名?>`（`ACT-REGISTRAR`）收取好處，把本應唯一的水牌孔位與簿頁號重複登記。他不知道所有下游買家，但清楚同號不可能自然出現。
3. 夜駝隊領隊 `<NPC#3@戰役:赤關水契: 姓?-名?>`（`ACT-NIGHT-CARAVAN`）把重複名額抽出的水袋運至九折關外轉運坡，再以陶罐短存。其核心利益是高抽成與保住隊員飯碗；風險升高時優先搬空藏水、燒掉私簿，不為掮客死戰。
4. 赤關水務掌案 `<NPC#4@戰役:赤關水契: 姓?-名?>`（`ACT-COVER-CLERK`）最初為應付春末驟增商旅，曾容許一批「先取水、後補牌」的臨時措施；他不是最初分贓者。但若在第三至第五篇已知道重號與缺口仍壓下重查，就轉成實質遮掩者。
5. 石背井堡老井戶 `<NPC#5@戰役:赤關水契: 姓?-名?>`（`ACT-WELL-WITNESS`）只知道近月夜間出水異常、白天井槽卻常不足。他擔心得罪商隊後失去生意，但也怕乾季死人；只要玩家不把井戶一概當共犯，他會逐步提供時段、車轍與藏水路線。

套利鏈實際運作：`合法名額 → 重號水牌 → 夜間超額出水 → 夜駝轉運 → 陶罐短藏／轉售 → 帳面以臨時補牌或次旬回填掩蓋`。任何單一環節都能被辯成「筆誤」「急用」「夜行避暑」或「商旅自備水」，但合起來會令合法駝隊在最需要時被拒水，並在大風封路前形成真實生命風險。

完整路線最後必須回答：誰重複出售名額、誰讓重號進簿、誰實際轉運與藏水、誰在知道缺口後選擇遮掩，以及如何在不關閉官井、不讓普通商旅斷水的前提下切斷套利鏈。

# 2. 跨篇既存時間線與條件式未來

## 玩家介入前已成立
- 春末商旅增加，水務掌案曾合法地允許一次臨時「先取後補」，留下可被濫用的程序縫隙。
- 掮客與井簿書吏之後把例外變成固定套利：重複水牌孔位與簿頁號。
- 夜駝隊已至少運過三次超額水；灰堰陶場外的廢窯坑已有短存陶罐。
- 老井戶知道夜間出水增加，但不知道完整責任鏈。

## 玩家完全不介入
- 白天合法駝隊被拒水的情況增多；
- 掮客為避查，會在第一場大風前加速搬走現有藏水；
- 水務掌案若看到缺口，會先選擇壓下重查以免赤關商路停擺；
- 風季來臨時，一條補給路被臨時柵控制，造成真正商旅在錯誤地點等待水。

## 條件式反應
- `duplicate_token_proof=true`：井簿書吏停止在東驛直接造新重號，改用舊頁補寫。
- `night_caravan_route=true`：夜駝隊改走九折關外轉運坡，縮短停留並預備搬空陶罐。
- `buried_cache_known=true`：掮客會把責任推成夜駝隊私賣，並要求在井路設「防盜」臨時柵，實際目的是控制誰能接近井堡。
- `registrar_link_proved=true`：水務掌案必須決定是否開正式重驗；若他壓下，`coverup_active=true`。
- `public_shortage=true`：任何「先別查、免得停商」主張的合理性下降，因短缺本身已成更大風險。
- `legal_water_plan=true`：第6篇可使用替代時段與護送水車，不需為查案關閉全部官井。

# 3. 戰役級 NPC registry

| 戰役 NPC key | actor_key | 身份／跨篇功能 | 首次正式登場 |
|---|---|---|---|
| `NPC#1@戰役:赤關水契` | `ACT-BROKER` | 配水掮客；套利核心受益者、後續反制者 | 第2篇被指向；第3篇可遠端施壓 |
| `NPC#2@戰役:赤關水契` | `ACT-REGISTRAR` | 東驛井簿書吏；重號入簿執行者 | 第1篇 |
| `NPC#3@戰役:赤關水契` | `ACT-NIGHT-CARAVAN` | 夜駝隊領隊；超額水轉運者 | 第2篇 |
| `NPC#4@戰役:赤關水契` | `ACT-COVER-CLERK` | 赤關水務掌案；先失職、後可能遮掩 | 第3篇訊息中出現，第5篇正面核心 |
| `NPC#5@戰役:赤關水契` | `ACT-WELL-WITNESS` | 石背井堡老井戶；時段與車轍證人 | 第1篇 |

以上號碼永久保留；後續階段如新增跨篇具體人物，必須先更新本 registry、遞增總劇本版本，再完成階段稿。

# 4. Campaign state 權威表

| state | 型別 | 初始值 | 來源／意義 |
|---|---|---:|---|
| `duplicate_token_proof` | bool | false | 是否取得可驗證的重號水牌／孔位證明 |
| `night_caravan_route` | bool | false | 是否知道超額水由夜駝隊轉運及大致路線 |
| `registrar_link_proved` | bool | false | 是否有證據把重號連回井簿書吏，而非只有市場傳聞 |
| `buried_cache_known` | bool | false | 是否定位九折關外陶罐藏水點 |
| `broker_link_proved` | bool | false | 是否有足夠資料連回配水掮客的重複出售／控制安排 |
| `coverup_active` | bool | false | 水務掌案是否在知道缺口後仍主動壓查 |
| `road_control_active` | bool | false | 第4篇三座臨時柵是否已形成對井路的實際控制 |
| `ledger_gap_proved` | bool | false | 是否在第5篇證明官面四十車級缺口 |
| `public_shortage` | bool | false | 合法商旅缺水是否已形成公開、可驗證事件 |
| `legal_water_plan` | bool | false | 是否建立不關閉全部官井的合法替代供水方案 |
| `broker_status` | enum | active | `active/exposed/captured/fled/dead` |
| `registrar_status` | enum | active | `active/cooperating/exposed/captured/fled/dead` |
| `night_leader_status` | enum | active | `active/cooperating/exposed/captured/fled/dead` |
| `cover_clerk_status` | enum | active | `active/cooperating/exposed/removed/dead` |

# 5. 六階段接口

## 第1篇《井堡水牌少了第七孔》
- 局部任務：在一支合法駝隊被拒水前，判明一枚水牌缺孔究竟是偽造、舊制差異或登簿錯誤，並讓井堡能安全決定是否放水。
- 局部真相：水牌本身是真的舊坯，被井簿書吏以重複孔位重新登簿；被拒駝隊不是偷水者。
- 主要輸出：`duplicate_token_proof`、`night_caravan_route`、`registrar_link_proved`、`public_shortage`。
- 可承接 ending：`water-token-chain-open`、`water-token-route-open` → 第2篇，`campaign_status=active`。
- 提早收束：`water-token-local-only` → `partly_completed (1/6)`；玩家解決眼前取水但沒有任何可追的重號／夜運接口。玩家可見戰役收束名「井水照流，舊孔無人問」。
- 放棄／濫權無接口：`failed (1/6)`。

## 第2篇《夜駝隊帶回兩套同號水袋》
### 解鎖條件
`S1 campaign_status=active` AND (`duplicate_token_proof=true` OR `night_caravan_route=true`)。解鎖結果只在第1篇結算時寫入 `campaign_save`，第2篇開場只載入已裁定結果。
- 局部任務：查清兩套同號水袋是補給重複、合法借袋還是夜間超額出水，避免錯抓普通駝工。
- 局部真相：夜駝領隊利用重號名額裝袋，將一套送正常商隊、一套送轉運坡；普通駝工只知道「夜裡多跑一趟」。
- 主要輸出：`night_caravan_route`、`buried_cache_known`、`broker_link_proved`、夜駝領隊狀態。
- 可承接：`duplicate-skins-ledger`、`duplicate-skins-witness` → 第3篇，`active`。
- 提早收束：`duplicate-skins-sealed-without-route` → `partly_completed (2/6)`；眼前雙號停止，但玩家沒有合法可追路線。玩家可見收束名「兩套水袋都回了架」。
- 放棄／蓄意錯責：`failed (2/6)`。

## 第3篇《九折關外埋著一車空陶罐》
### 解鎖條件
`S2 campaign_status=active` AND `night_caravan_route=true` AND (`buried_cache_known=true` OR S2 ending=`duplicate-skins-witness`)。
- 局部任務：在藏水被搬空前確認陶罐用途、保住井路供水、判明上游誰下單。
- 局部真相：陶罐是短存水，不是毒物或走私酒；夜駝隊按掮客提供的重號名額搬運，水務掌案尚未直接分贓。
- 輸出：`buried_cache_known`、`broker_link_proved`、`registrar_link_proved`、`public_shortage`，並決定是否觸發 `road_control_active` 的第4篇反應。
- 可承接：`buried-jars-chain-proved`、`buried-jars-cache-secured` → 第4篇，`active`。
- 提早收束：`buried-jars-taken-private` → `partly_completed (3/6)`；藏水被處理但責任鏈無法公開追。玩家可見收束名「空罐埋回風沙」。
- 放棄／錯責：`failed (3/6)`。

## 第4篇《長風井路一夜多了三座臨時柵》
### 解鎖條件
`S3 campaign_status=active` AND (`broker_link_proved=true` OR `buried_cache_known=true`)。
- 直接使用 NPC：`NPC#1@戰役:赤關水契`、`NPC#5@戰役:赤關水契`；若井簿書吏仍可合作，可作制度證人但不是唯一來源。
- 為甚麼發生：掮客或其代理人以「防盜、分流」名義設三柵，實際控制誰能接近井堡與轉運點；若前篇 `road_control_active=false`，則改成「施工被阻但授權爭議未清」，三個預定位置仍形成通行衝突，而不是無條件強迫三柵已建成。
- 玩家理由：此前已被正式記為重號／藏水調查協作者，或持有第3篇已結算證據。
- 局部任務：在不封死合法商旅的前提下拆解三柵的實際授權、保留必要的夜間分流安全措施，並建立可運行的合法替代供水時段。
- 局部真相：第一柵由井堡依舊例設置且合法；第二、第三柵只有掮客代理人的私約，無權限制官道取水。全拆會讓牲口、水車與候水商旅在夜間同路衝突；全留則令掮客掌握入口。
- 可改變 state：`road_control_active`、`legal_water_plan`、`broker_link_proved`、`public_shortage`。
- `ending_id: three-barriers-lawful-route`：兩座越權柵被撤／失效，合法分流保留，`broker_link_proved=true`、`legal_water_plan=true`、`campaign_status=active` → 第5篇。
- `ending_id: three-barriers-proof-with-shortage`：授權鏈已證明但供水仍短缺，`broker_link_proved=true`、`public_shortage=true`、`campaign_status=active` → 第5篇。
- `ending_id: three-barriers-local-peace`：只把道路衝突壓下，未保存官簿／掮客責任接口，`partly_completed (4/6)`；玩家可見收束名「三道柵只剩一道」，眼前恢復通行，後續帳責無合法接口。
- `ending_id: three-barriers-closed-road`：以私力封死合法井路或造成可避免的供水中斷，`failed (4/6)`。
- `ending_id: three-barriers-abandon`：任務放棄，`failed (4/6)`。

## 第5篇《赤關水簿少了四十車》
### 解鎖條件
`S4 campaign_status=active` AND (`broker_link_proved=true` OR `registrar_link_proved=true`) AND (`legal_water_plan=true` OR `public_shortage=true`)。
- 直接使用 NPC：`NPC#2@戰役:赤關水契`（若仍可出面）、`NPC#4@戰役:赤關水契`；掮客依 status 正面、逃亡或以代理資料存在。
- 為甚麼發生：第4篇已令井路授權／短缺問題無法只當地方糾紛，赤關必須把地方分簿、臨時補牌與城內總簿對回；表面少四十車不是四十車實體同時失蹤，而是多種重複計數與未回填缺口疊加。
- 玩家理由：已在前篇保存正式可核對資料，且其建立的供水替代方案或公開短缺讓官面無法只封井停查。
- 局部任務：把井堡出水、臨時補牌與總簿對回，區分重號套利、合法例外、單純遲登與掌案收到證據後的主動遮掩。
- 局部真相：四十車級帳面差由重號套利與早期合法例外共同造成；水務掌案最初不是分贓者，只有在收到足夠證據後仍壓下重驗才使 `coverup_active=true`。
- 可改變 state：`ledger_gap_proved`、`coverup_active`、`cover_clerk_status`、`broker_status`、`registrar_status`、`legal_water_plan`。
- `ending_id: forty-carts-audit-open`：缺口與責任層次均證明、供水方案仍可運作，`ledger_gap_proved=true`、`campaign_status=active` → 第6篇。
- `ending_id: forty-carts-coverup-proved`：掌案在知情後的遮掩被證明，且有替代供水／公開短缺接口，`coverup_active=true`、`ledger_gap_proved=true`、`campaign_status=active` → 第6篇。
- `ending_id: forty-carts-books-balanced-only`：只把帳面補平但上游責任與末篇供水資格均未留下，`partly_completed (5/6)`；玩家可見收束名「四十車回到紙上」，帳面恢復、風前最後一口官井仍按舊規運作但本戰役不再自動承接。
- `ending_id: forty-carts-destroyed-ledger`：蓄意毀掉唯一可核對總簿且未保留替代來源，令責任鏈無法合理收束，`failed (5/6)`。
- `ending_id: forty-carts-abandon`：任務放棄，`failed (5/6)`。

## 第6篇《沙海第一場風前的最後一口官井》｜末篇
### 解鎖條件
`S5 campaign_status=active` AND `ledger_gap_proved=true` AND (`legal_water_plan=true` OR `public_shortage=true`)。
- 直接使用 NPC：所有仍存活／可聯絡的戰役級 NPC；死亡、逃亡或合作狀態不得重置。沒有單一 NPC 是末篇唯一情報源。
- 為甚麼發生：第一場大風預計在一日內封住長風沙海邊緣部分路線，最後一批合法商旅、涉案水車與證據押運同時爭用最後一口官井；查案與供水不能再分開處理。
- 玩家理由：此前已證明總簿缺口並保存至少一條合法供水／公開短缺接口，因此有現實資格介入最後調度，而不是只因「主角必須到場」。
- 局部任務：在風前同時處理合法供水、商旅撤離、涉案人物／證據去向與重號制度終止，不能用關閉所有官井作唯一解答。
- 核心真相接觸：掮客負重複出售與套利組織責任；井簿書吏負明知重號入簿責任；夜駝領隊負知情轉運與隱瞞責任；水務掌案只為自己的早期程序失職與「知情後是否遮掩」負責，不能被倒寫成最初主謀。
- `ending_id: last-well-chain-broken`：合法旅隊得水／撤離、證據足以區分四層責任、重號程序被切斷，`campaign_status=completed (6/6)`。
- `ending_id: last-well-water-saved-case-thin`：供水與撤離成功，但部分人證／總簿證據失去，仍足以停止重號而無法完整追究所有人物，`campaign_status=partly_completed (6/6)`；玩家可見收束名「風前有水，帳上留白」，明確說明哪些責任未能坐實。
- `ending_id: last-well-case-won-water-lost`：玩家保住責任證據卻因可避免的錯誤調度造成合法商旅嚴重缺水／滯留；制度案可追但戰役核心「查案不斷水」失敗，`campaign_status=failed (6/6)`。
- `ending_id: last-well-abuse`：無必要以暴力或私權奪井、令普通商旅成為代價，`campaign_status=failed (6/6)`。
- `ending_id: last-well-abandon`：末篇放棄，`campaign_status=failed (6/6)`。

# 6. Actor 反應規則

## ACT-BROKER
- 初始知道／不知道：知道重號、夜運、陶罐短存與自己的客戶；不知道玩家每篇究竟保存了哪些證據，也不知道水務掌案最後會否替他壓查。
- 核心利益：保持代辦水牌的市場地位、現銀與商旅關係。
- 當前計畫：在重號未被公開坐實前繼續套利；曝光後切斷新重號、推責夜駝隊並以井路「防盜」控制接近證據的人。
- 資源：多支合法客戶、普通跑腿、貨簽、現銀與可否認的口頭委託；**沒有官府指揮權**，不能合法命井堡封路。
- 限制：不掌握官印、無法強迫所有客戶同口供；逃亡會失去本地代辦網。
- 改變條件：`broker_link_proved=true` 時由否認轉推責；`ledger_gap_proved=true` 時優先逃離、交易或自保供詞。
- 可觀察反應：停止造新牌、搬空藏水、派柵木車、改約見地點、要求跑腿傳「不要走舊坡」。

## ACT-REGISTRAR
- 初始知道／不知道：知道自己讓重號入簿；不知道全部下游買家與藏水點。
- 核心利益：避免失職／受賄曝光並保住差事。
- 當前計畫：先把重號說成舊制重登；若壓力增大，以草簿或供詞換取區分責任。
- 資源：井簿、草簿、舊存根存取權與對地方程序的熟悉；沒有權力單獨改總簿。
- 限制：實物存根、他人木籌與墨色刮改不受其完全控制。
- 改變條件：`duplicate_token_proof=true` 後停止造新重號；若公開定罪而證據不足，先毀草簿後逃；若玩家提供可區分責任的出路，可合作。
- 可觀察反應：由「牌無效」退成「舊制重登」、交草簿、撕角頁、求井堡援手。

## ACT-NIGHT-CARAVAN
- 初始知道／不知道：知道夜運、掮客暗記與短存點；不知道官面上層是否知情。
- 核心利益：保住隊員、抽成與退路。
- 當前計畫：在袋號未曝光時繼續夜運；曝光後先搬空藏水、分散普通駝工，再視 PC 是否區分責任決定合作。
- 資源：駝隊、貨簽、夜路經驗、私簿與搬運工關係；沒有造水牌或改官簿權力。
- 限制：牲口傷病、駝工目擊、袋號與陶罐批記會留下獨立痕跡。
- 改變條件：玩家不把普通駝工當共犯時更可能合作；全面無證據拘押時更可能毀簿／離城。
- 可觀察反應：燒私簿、隊員四散、交路線、帶看貨簽或出城改道。

## ACT-COVER-CLERK
- 初始知道／不知道：知道自己曾容許一次合法例外；前兩篇不知道完整重號鏈，第三篇起才可能正式收到證據。
- 核心利益：商路不停、自己不因程序失職被撤，同時維持官面可運作。
- 當前計畫：證據不足時先維持供水並延後全面重驗；證據足夠時在「開查」與「壓查」間作出可被玩家觀察的決定。
- 資源：調閱地方分簿、安排官面重驗、發布臨時供水時段的行政權；不能憑空消除已流出的副本與民間證人。
- 限制：若 `legal_water_plan=true`，其「一查就會停商」理由失去主要基礎；若 `public_shortage=true`，繼續壓查本身造成更大行政風險。
- 改變條件：收到足夠重號／夜運證據仍壓查才使 `coverup_active=true`；若選擇合作則 `cover_clerk_status=cooperating`。
- 可觀察反應：發重驗令、要求延後、召回總簿、壓下副本或公開承認早期例外程序。

## ACT-WELL-WITNESS
- 初始知道／不知道：知道夜間出水多、白天不足與部分車轍時段；不知道重號、掮客完整身份與官面責任。
- 核心利益：井堡生計、旅客安全與避免全井被封。
- 當前計畫：先守住井堡正常運作，只在相信玩家不會一概封井時提供更多觀察。
- 資源：長期時段記憶、木籌、井戶人脈與現場操作知識；沒有官面決策權。
- 限制：只能證明自己看見／記錄的夜間出水，不能證明上游收賄。
- 改變條件：玩家保護普通井戶與合法供水時合作加深；要求全封井時轉為抵抗。
- 可觀察反應：交木籌、說駝鈴方向、帶看車轍、召其他井戶作證或拒絕再開庫。

# 7. 跨篇證物／物品

- `EVID-WATER-TOKEN-A`：第1篇重號水牌與孔位拓印；可被保存為玩家可見結算資料。
- `EVID-NIGHT-LEDGER`：第2篇夜駝簡簿；若失去，可由領隊合作或第3篇陶罐批記替代，不能無限重生。
- `EVID-JAR-MARKS`：第3篇陶罐底批記與沙地車轍對應；指向轉運鏈，不單獨證明官面遮掩。
- `EVID-MASTER-LEDGER`：第5篇赤關總簿；末篇核對核心責任的重要來源，但若毀損仍可由前述證據＋多井堡分簿形成較弱結論。

# 8. 提早戰役結局最低收束

任何 `partly_completed` 都必須先收住當篇眼前危機，再留下不劇透尾巴；不得用「待續」代替結算。
- 1/6「井水照流，舊孔無人問」：合法駝隊得水，井堡恢復秩序；尾聲只描述夜裡仍有一串無燈駝鈴經過遠坡。
- 2/6「兩套水袋都回了架」：雙號停止、被錯疑者澄清；尾聲只見遠處有人搬走空陶罐，無玩家可合法追蹤的接口。
- 3/6「空罐埋回風沙」：藏水已不再危及當日旅隊，但責任證據被私人處理；尾聲是新柵木運上井路，玩家沒有足夠已結算接口自動續篇。
- 4/6「三道柵只剩一道」：越權通行衝突已消失，合法分流仍在；玩家看見赤關方向有人收走一疊舊水簿，但沒有已結算官簿接口可自動續篇。
- 5/6「四十車回到紙上」：帳面已被補平、短期供水秩序恢復；風前最後一口官井仍會照舊開放，但責任鏈不再由本戰役自動承接。
- 6/6「風前有水，帳上留白」：最後一批合法旅隊完成取水與撤離、重號程序停止；GM 明確結算哪些人物責任因證物失去而只能保留未證明，戰役仍以 `partly_completed` 正式結束。

# 9. 作者續寫約束

- 第4–6篇不得推翻前三篇已成立的局部責任；井簿書吏不是無責傀儡，夜駝領隊也不是唯一幕後。
- 新增戰役級 NPC 前先更新本總劇本 registry。
- 任何較早 state 若仍參與後篇解鎖，必須在該篇接口保留，不得只看緊接前一篇。
- 所有非末篇正式 ending 均需明列可承接／提早戰役結局與 campaign_status 映射；正式階段稿可增加局部 ending 變體，但不得改變總劇本已固定的主要因果邊界。
- 第6篇為正式末篇；末篇後普通世界餘波可存在，但不另開原戰役第7篇。