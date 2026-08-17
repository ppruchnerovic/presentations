---
id: 930
title: "When Value Becomes Programmable: A Developer's Guide to Tokenization"
slug: when-value-becomes-programmable-a-developer-s-guide-to
event: "World Congress 2026 Berlin"
event_slug: wwc-2026-berlin
track: "Emerging Technologies"
type: "Keynote/Talk"
stage: "Stage 7"
tags: ["Cryptography", "FinTech", "Infrastructure", "Smart Contracts"]
speakers: ["Luke Forrest"]
speaker_companies: ["Hashgraph"]
day: 2
starts_at: 2026-07-10T11:00:00+00:00
duration_min: 30
recording_url: https://www.youtube.com/watch?v=7fo0t96oRB8
video_id: 7fo0t96oRB8
session_page: https://app.wearedevelopers.com/events/16/session/930
transcript: true
---

# When Value Becomes Programmable: A Developer's Guide to Tokenization

**Luke Forrest (Developer Relations Engineer — Hashgraph)**

`Track: Emerging Technologies` · `Type: Keynote/Talk` · `Stage: Stage 7`

`#Cryptography` `#FinTech` `#Infrastructure` `#Smart Contracts`

[Watch the recording](https://www.youtube.com/watch?v=7fo0t96oRB8) · [Session page](https://app.wearedevelopers.com/events/16/session/930)

## Abstract

The internet made information programmable. Tokenization is doing the same for value and ownership, and it has quietly moved from speculation to infrastructure: stablecoins now settle real payment volume at global scale, and tokenized real-world assets, from treasuries to funds, are measured in billions and climbing. For developers, that shift opens a design space we have never really had. Applications where payments, ownership, royalties, access rights, and provenance live inside the asset itself, settling instantly and globally without a stack of intermediaries reconciling ledgers behind the scenes. This talk starts with why that matters and what it means for the things you can build.

From there it gets practical: what a token actually is, the two ways to issue one (as a smart contract or as a native protocol primitive), and the trade-offs between them in flexibility, cost, and attack surface. We'll make it concrete on Hedera, using its token service to create and govern assets, both fungible and non-fungible, without writing Solidity, and showing how those native tokens still compose with smart contracts when you need custom logic. You'll leave understanding not just how tokenization works, but why it is becoming core developer infrastructure and where the opportunity is to build on it.

## Speakers

### Luke Forrest

*Developer Relations Engineer — Hashgraph*

Luke is a Developer Relations Engineer at Hashgraph, working directly with projects building on Hedera to make sure they have the tools, guidance, and support they need to build. Luke’s day-to-day is spent alongside builders: unblocking integration issues, feeding their requirements back into our SDKs and docs, and connecting them with the right people across the ecosystem. He has been working in DLT since 2020, across multiple projects tokenising real-world and financial assets, which keeps him close to the practical challenges teams hit when value starts moving on-chain.

## Transcript

*2,190 words · source: yt (en)*

**[0:03](https://www.youtube.com/watch?v=7fo0t96oRB8&t=3s)** Hi everyone, I'm Luke and I work on developer relations at Hashgraph. And over the next 25 minutes or so, I want to convince you of just one thing. That the next 30 years of finance are going to look completely different to the last 30. So here's what we're going to cover. Five things. What is tokenization? Who is using tokenization? Who's driving that growth? And how you can get started. And then some tools you can use to build something this weekend if you like. So 30 years ago, information was paper, letters, books, newspapers, files and cabinets. To share something, you copied it physically. To find something, you went somewhere. Then the information made sorry then the internet made that

**[0:52](https://www.youtube.com/watch?v=7fo0t96oRB8&t=52s)** information programmable. Now anyone can copy, search, transform, and share information instantly. The web didn't make that information more important, just changed what was possible with it. And tokenization is doing the exact same thing, but but for value and ownership. Stocks, bonds, dollars, real estate, identity. Things that used to require lawyers, custodians, registries, settlement systems are all becoming programmable objects on an open network. Same revolution, different layer of the stack. So, what is a token really? Most people define a token as a digital representation of value. And that's true, but it's more than just a representation of value. Every traditional asset depends on three

**[1:39](https://www.youtube.com/watch?v=7fo0t96oRB8&t=99s)** separate systems. The asset itself, a record of who owns it, and a way to transfer it from one owner to another. Take a dollar for example, the physical currency. You need a database row at your bank to show how much you have. And then you need Swift to move it. A US Treasury, you need the bond, a custodian's record, and then Clearstream to settle that trade. A real estate investment trust share, you need the share, a transfer agent's record, your broker plus DTCC to transfer it. And a token collapses all of those three things into a single object. the assets, the ownership record and the transfer mechanism are now all the same thing. USDC, for example, a digital dollar

**[2:28](https://www.youtube.com/watch?v=7fo0t96oRB8&t=148s)** isn't just a representation of a dollar somewhere else. It is the dollar. It's the record, the transfer rail, all unified into a single object. And so that's what tokens actually are. And let's have a look at what's happening today. Who's using this and how fast it's growing. So if you have a look at this graph here, these are real payments. Each one is under $10,000 and over a dollar. These are all remittances, payroll, B2B invoices, the kind of transactions that actually move money around the world. There's 60 million in early 2024 and over 300 transactions a month today. That's a 6x growth in two years. Almost all of it is USDT and USDC tokenized dollars. Real users, real transactions,

**[3:18](https://www.youtube.com/watch?v=7fo0t96oRB8&t=198s)** real volume. So if we look at this from a different lens, this is the volume, how many transactions are taking place. And this is how much value is actually moved. An average of $250 billion a month today. And that transfer volume doubled in 18 months. So at the minute, this is one of the fastest growing payment rails in history. So let's take a look at who's actually driving this, who's tokenizing. And there's there are two main groups. Those that are tokenizing the asset and those that are using the rails. For example, Black Rockck's Breedle Fund, it's 2.5 billion in AUM in tokenized T bills. Franklin Templeton, an onchain money market fund since 2021. Apollo 100 million plus in tokenized private

**[4:08](https://www.youtube.com/watch?v=7fo0t96oRB8&t=248s)** credits and then you also have JP Morgan, Goldman Sachs, NASDAQ are all currently building tokeniz tokenization infrastructure today. Stripe bought bridge for $1.1 billion. Visa has about $7 billion today in annualized stable coin settlement. And then Mastercard recently acquired BVNK for 1.8 billion. BVNK is a wallet as a service provider and a payment service provider. And then there's one institution doing both already on Hideera and that's Archax. It's the first regulated uh sorry FCA regulated digital asset exchange. So they're both tokenizing funds from Black Rockck, Abedine, LNG, State Street, and then streaming the yield of those funds in USDC.

**[4:58](https://www.youtube.com/watch?v=7fo0t96oRB8&t=298s)** And 60% of that pay stable coin payment volume in 2025 was all B2B. So this isn't just me sending you a stable coin and counting that volume is businessto business operations. So let's take a look at where the banks think it will go. Today, there's about $334 billion market cap in stable coins and real world assets. And McKenzie's conservative estimate is $2 trillion by 2030. City Bank says about 6 12 trillion, BCG 16 trillion, and Standard Charted 30 trillion. And as you can see, their forecasts are a bit different. But if you go with Cityroup's um estimate as it includes stable coins, not just real world assets, which I

**[5:48](https://www.youtube.com/watch?v=7fo0t96oRB8&t=348s)** showed earlier, it's a 19x growth in the next four years. The beauty of this is you don't just have to take my word for it. You have Larry Frink, the CEO of BlackRock. uh he said every stock, every bond, every fund, every asset can be tokenized and if they are, it'll revolutionize investing. And then you also have Paul Atkins, chairman of the SEC. He said firms from household names on Wall Street to unicorn tech companies in Silicon Valley are all lined up at their doors with requests to tokenize. And when you have the biggest asset manager on earth and the regulator who decides whether or not this is legal, both saying the same thing, the question isn't whether this happens, it's who builds it. And so, how do we tokenize? And before I

**[6:37](https://www.youtube.com/watch?v=7fo0t96oRB8&t=397s)** show you any code on how to create a token, I'm going to run you through what tokenization actually requires to ensure a successful outcome. Throughput at scale. So Visa, for example, currently peaks at about 24,000 transactions per second. And you might not need that for a tokenized asset right now, but they need to know it's possible and can scale. You need finality in seconds. You can't have proper ballistic confirmations. No wait for 12 blocks. You need deterministic settlement. When the transaction is done, it's done in sub 10 seconds. You need predictable fees. Banks can't budget for gas fees. They can't budget for when a network is congested and the fees go up. They need to be fixed to the dollar so they can forecast. Developer

**[7:26](https://www.youtube.com/watch?v=7fo0t96oRB8&t=446s)** familiarity, the tools your team already uses, JavaScript, Go, Swift, Python, and if you're familiar with EVM, Solidity, Hardat, Metam Mask, you also need regulated governance. The institutions who are tokenizing on the network need to know where the validators are running. You can't have a validator running in a sanctioned c country and have your tokenized asset pass through that validator. And you also need energy efficiency. Banks have ESG mandates. Networks that are proof of work that burn megawws of power per transaction won't work. Most chains can do two or three of these and Cadera can do all six. And so you don't actually have to be a

**[8:15](https://www.youtube.com/watch?v=7fo0t96oRB8&t=495s)** web 3 developer to be able to create a token. If you can build or integrate with Stripe, you can tokenize on Hideera. So this is 10 or so lines of code in JavaScript to create a tokenized asset. And in terms of fees, it's only a dollar to create the asset and one cent to transfer. So that's about 10,000 transactions for $100. So it's incredibly cheap and that's pegged to the dollar so it won't change depending how congested the network is. And if you don't like JavaScript, we also have Python, Java, Go, Swift, and other community supported SDKs. And so what do tokens actually make possible? I showed you how to create a

**[9:04](https://www.youtube.com/watch?v=7fo0t96oRB8&t=544s)** token in the smallest amount of lines of code possible, but there are six capabilities that are built into the network to help you govern the network. So, identity, for example, only verified holders should be able to receive your tokenized asset. So, once they complete KYC, you can approve their account to be able to receive that tokenized asset. compliance. You need to be able to freeze certain accounts on legal order. If sanctions are updated or court orders come in, you need to or fraud gets discovered, you can respond with a single transaction on the network to freeze a particular account. economics. For example, if you want to set custom

**[9:51](https://www.youtube.com/watch?v=7fo0t96oRB8&t=591s)** fees on your token, so every time it's transferred, you want to receive a percentage of the sale or amount moved, you can build that into your token life cycle. You need to be able to add more tokens to circulation. For example, if a stock split happens, you need to be able to mint more tokens and distribute those to existing holders. And then control, you need to be able to halt all activity instantly. Emergency response, for example. And then data, you need to be able to update the token's metadata. What is actually said about the token? And every single one of these is an SDK method um that you can build into your application.

**[10:39](https://www.youtube.com/watch?v=7fo0t96oRB8&t=639s)** And so one more example of how you can create a token. So this QR code will take you to Hideera's developer portal directly to this page which will allow you to create a token on testnet instantly today. All from your browser. No having to install any um any packages. It works all in browser. All you need to do is create an account and click the button to tokenize. And if you're interested in more than just tokenization as well, there's plenty of other options for you to choose from on everything you can do and build on Hideera from Hideera consensus service to smart contract service. I will bring this QR code back at the end as well. And the developer portal is an

**[11:26](https://www.youtube.com/watch?v=7fo0t96oRB8&t=686s)** incredibly easy place to have a play around with Hideer and see what's possible in web 3 and creating a token for example. And now I'm going to show take it one step further and show some other tooling that you can use to tokenize today. First up is asset tokenization studio. And I will have some QR codes at the end for this. But this is an open-source toolkit that you can clone and spin up on test net or mainet if you wanted to. Has pre- audited smart contracts for you to be able to tokenize. Comes with the TypeScript SDK as well as wallet support. And you can add to this as well if you want to if you wanted to build some custom modules. And we also have one use case using this today. Red Swan. They currently have about a 5 billion

**[12:14](https://www.youtube.com/watch?v=7fo0t96oRB8&t=734s)** commercial real estate portfolio all tokenized on Hyera using asset tokenization studio. And then if you're more interested in stable coins for example, there's also stable coin studio. And this is for issuing and managing regulated stable coins. It has built-in proof of reserve which means your stable coin would be aligned with Genius and and the Micah uh regulations as well as KYC and anti-money laundering integrations. So you can integrate KYC into the application and this is also being used in production today by the Australian uh reserve bank through project acacia and they're working with Australian payments plus uh to create the

**[13:02](https://www.youtube.com/watch?v=7fo0t96oRB8&t=782s)** Australian dollar. And then one more tool that you can use as well is Aetto. And Aetto is the commercial version of asset tokenization studio. It was built by IO Builders in partnership with Hashgraph with an end-to-end platform for the full tokenized asset life cycle in issuance, bonds, equities, money market funds, loans. All you need to do is spin it up, configure it, and if you wanted more out of the tool, you can use custom plugins to take it one step further. It also has primary and secondary markets built into it. Listings, order books, requests for

**[13:51](https://www.youtube.com/watch?v=7fo0t96oRB8&t=831s)** quotes, bilateral trades, the full market micro structure. An asset tokenization studio which I showed you before. If you think of that as the issuance toolkit and aetto gives you the full asset life cycle all with t plus0 atomic settlement which means when a trade is submitted and settled it's all sub 10 seconds. no waiting 2 or 3 days for the trade to complete all with Hideera as the underlying backbone. So, I'll put some QR codes up on the screen there if any of those tools interest you or you want to learn more. And if there's any questions about Tokenization Studio, I'm happy to take those now or if you wanted to come find me at the booth later, I'm

**[14:39](https://www.youtube.com/watch?v=7fo0t96oRB8&t=879s)** happy to discuss with you. Nope. >> Cool. Um, I'll leave those up on the screen for a minute. Um, but, uh, that's the end of the talk. Thanks very much and thank you all for coming. [applause]
