# 戰役總劇本：漕印沉沙

- campaign_id：OOTB-CAMPAIGN-CAOYIN-CHENSHA-001
- 版本：1.0.1
- 狀態：連載中
- 地區：承泰二十一年，河洛道洛安以北；北倉鎮、石門渡、洛安北郊為本戰役新增地方地點。
- 規劃：四個中型階段，角色約4–9級。
- 作者稿進度：01《北倉七枚封泥有一枚沒有官紋》已完成並通過單篇 Phase B；02–04 待續寫。

## 跨篇真相
北倉近兩月的封泥錯紋、空車補簿與夜間短駁，來自地方糧運侵吞網：每批抽走少量新糧，再以陳糧補足帳面重量。轉運書吏 NPC#1 掌握簿冊、封泥與交接時點；承運人 NPC#2 把最初的臨時侵吞擴成固定貨路。渡工頭 NPC#3 知道未登簿夜渡但誤以為只是逃稅；驗糧老手 NPC#4 能以留樣證明同批糧並非同源。

若無玩家介入，七日內最後一批新糧被轉走，NPC#1 燒掉私記並把錯紋歸咎學徒；半月後陳糧在雨季前入倉，NPC#2 離開北倉，NPC#1 承擔大部分官面責任。

## 戰役 NPC registry
- <NPC#1@戰役:漕印沉沙: 姓?-名?>；actor_key=ACTOR_LEDGER_CLERK；北倉轉運書吏。利益：保職、保家人、不獨自背責。第一階段登場。
- <NPC#2@戰役:漕印沉沙: 姓?-名?>；actor_key=ACTOR_CARRIER；地方承運人。利益：維持抽糧貨路、切斷實物與人證。第二階段正式登場。
- <NPC#3@戰役:漕印沉沙: 姓?-名?>；actor_key=ACTOR_FERRY_FOREMAN；石門渡渡工頭。知道三次夜渡日期與方向，不知換糧全貌。第一階段登場。
- <NPC#4@戰役:漕印沉沙: 姓?-名?>；actor_key=ACTOR_GRAIN_EXAMINER；驗糧老手。保存三份糧樣與炭筆記號。第一階段登場。

## campaign state
C01_seal_anomaly=unknown/documented/destroyed；C02_night_ferry=unknown/located/witnessed；C03_grain_samples=none/partial/secured；C04_clerk_stance=denial/bargaining/cooperating/unavailable；C05_carrier_alert=0..3；C06_private_warehouse=unknown/suspected/confirmed/emptied；C07_public_accountability=private/local_official/public；C08_campaign_status=active/partly_completed/failed/completed；C09_next_stage_unlock 保存上一階段結算時已裁定的下一階段，不在後篇開局重算。

## 跨篇證物
PROP-CAM-01 錯紋封泥；毀損後只能由領泥差額與殘蠟證明曾重封。PROP-CAM-02 封泥領用簿；毀損後由盤存與值守交接重建時段。PROP-CAM-03 三份糧樣；被帶走或交官後按 campaign_save 實際位置承接；全毀則只能用麻袋縫線與蟲殼作較弱證據。PROP-CAM-04 短駁船租欠條；毀損後以木樁纜痕與排班證明至少一次夜航。

## 階段接口
1. 北倉七枚封泥有一枚沒有官紋（4–6級，R5）：查明重封、異糧與石門渡方向。可承接：A=C01 documented AND C02 located；B=C03 secured AND C04 bargaining/cooperating；C=C03 partial 且取得明確渡口方向。放棄或所有來源永久失去且接受疏失結案則提早收束。
2. 石門渡三艘短駁有一艘從不點燈（5–7級，R6）：只讀 C09=stage2；定位私人倉棧或上游車隊。買斷停查／放棄則 partly_completed(2/4) 或 failed。
3. 洛安北郊兩座糧倉只開一座正門（6–8級，R7）：只讀 C09=stage3；保糧、保證據、控人三者取捨。若同時阻止最後換糧、控制 NPC#2 並取得完整責任鏈，可 completed(3/4)；仍有最後陳糧或責任問題才進第四篇。
4. 北倉雨前最後一冊驗收簿（7–9級，R8）：只讀 C09=stage4；末篇處理不同 NPC 存亡、證物位置與責任鏈，所有 ending 正式收束。

## 跨篇例外
NPC#1 不可用時，以領用簿、交割抄條與工作時段承接；無抄條只能走部分責任線。NPC#2 提前被捕時，不重置貨路，改查已發車船；若責任鏈已完整可提早成功。NPC#3 不可用時用欠條、排班、木樁；不得生成換皮全知渡工。NPC#4 不可用時用留樣與炭筆記號；樣本亦全毀則降為弱證據線。玩家提前公開懷疑使 C05 至少+1，後篇改追搬運痕跡，不重置倉棧。

## ending 承接原則
每個非末篇 ending 必須在相應階段正文標成「可承接」或「提早戰役結局」。放棄一律中斷。partly_completed 必須先收住當篇實際成果，再以玩家可見但不揭 GM 真相的缺口作最後一拍；該缺口不自動解鎖下一篇。
