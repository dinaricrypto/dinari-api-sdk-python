# Reference

## Market Data

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_alloys</a>(...) -> PaginatedAlloyResponseV1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns available `Alloys` with cursor-based pagination.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_alloys()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — If set, this endpoint will return Alloys that match the symbols specified

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAlloysRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_alloy_current_price</a>(...) -> AlloyPriceV1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current price for a specified `Alloy`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_alloy_current_price(
    alloy_id="alloy_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alloy_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_alloy_price_chart</a>(...) -> typing.List[AlloyHistoricalPriceDataPointV1]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get historical price data for a specified `Alloy`. Each index in the array represents a single tick in a price chart.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_alloy_price_chart(
    alloy_id="alloy_id",
    timespan="DAY",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alloy_id:** `str`

</dd>
</dl>

<dl>
<dd>

**timespan:** `GetAlloyPriceChartRequestTimespan` — The timespan of the historical prices to query.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_stocks</a>(...) -> GetStocksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of `Stocks`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_stocks()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of `Stock` symbols to query. If not provided, all `Stocks` are returned.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetStocksRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_stock_current_price</a>(...) -> StockPrice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current price for a specified `Stock`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_stock_current_price(
    stock_id="stock_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stock_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_stock_current_quotes_route_v2</a>(...) -> StockQuoteResponseOneOfSchema</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get quote for a specified `Stock`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_stock_current_quotes_route_v2(
    stock_id="stock_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stock_id:** `str`

</dd>
</dl>

<dl>
<dd>

**feed:** `typing.Optional[MarketDataFeed]`

Requested data source for the quote. Only applies when using x-api-version: 2.
Allowed values:

- `null`: (default) Selects the highest quality available free data source.
- `sip`: Consolidated quote from all U.S. exchanges (NBBO). This is a paid data source and incurs usage-based billing.

</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` — Entity id of customer requesting quote. Required to use sip feed. If this is an internal query, supply your organization entity_id

</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — Version for this method

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_stock_price_chart</a>(...) -> typing.List[StocksHistoricalPriceDataPoint]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get historical price data for a specified `Stock`. Each index in the array represents a single tick in a price chart.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_stock_price_chart(
    stock_id="stock_id",
    timespan="DAY",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stock_id:** `str`

</dd>
</dl>

<dl>
<dd>

**timespan:** `StockTickTimespan1` — The timespan of the historical prices to query.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_stock_news_by_stock_id</a>(...) -> typing.List[StockNewsArticleInfo]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the most recent news articles relating to a `Stock`, including a summary of the article
and a link to the original source.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_stock_news_by_stock_id(
    stock_id="stock_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stock_id:** `str`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of articles to return.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.market_data.<a href="src/dinari/market_data/client.py">get_market_hours</a>() -> ExtendedMarketHours</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the market hours for the current trading session and next open trading session.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.market_data.get_market_hours()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Corporate Actions

<details><summary><code>client.corporate_actions.<a href="src/dinari/corporate_actions/client.py">get_stock_splits</a>(...) -> GetStockSplitsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of stock splits for `Stocks` available for trade via Dinari.
The splits are ordered by the date they were created, with the most recent split first.

In an example 10-for-1 stock split, trading will be halted for the stock at the end of the `payable_date`, as
the split transitions from `PENDING` to `IN_PROGRESS`. This usually occurs over a weekend to minimize trading
disruptions. Each share of stock owned by a shareholder will then be converted into 10 shares, and the split
becomes `COMPLETE` as trading resumes on the `ex_date` with new split-adjusted prices.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.corporate_actions.get_stock_splits()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetStockSplitsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.corporate_actions.<a href="src/dinari/corporate_actions/client.py">get_stock_splits_by_id</a>(...) -> GetStockSplitsByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of stock splits for a specific `Stock`.
The splits are ordered by the date they were created, with the most recent split first.

In an example 10-for-1 stock split, trading will be halted for the stock at the end of the `payable_date`, as
the split transitions from `PENDING` to `IN_PROGRESS`. This usually occurs over a weekend to minimize trading
disruptions. Each share of stock owned by a shareholder will then be converted into 10 shares, and the split
becomes `COMPLETE` as trading resumes on the `ex_date` with new split-adjusted prices.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.corporate_actions.get_stock_splits_by_id(
    stock_id="stock_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stock_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetStockSplitsByIdRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.corporate_actions.<a href="src/dinari/corporate_actions/client.py">get_stock_dividends_by_stock_id</a>(...) -> typing.List[StockDividendAnnouncementDetail]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of announced stock dividend details for a specified `Stock`.

Note that this data applies only to actual stocks. Yield received for holding tokenized shares may differ from this.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.corporate_actions.get_stock_dividends_by_stock_id(
    stock_id="stock_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stock_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Entities

<details><summary><code>client.entities.<a href="src/dinari/entities/client.py">get_entities</a>(...) -> GetEntitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of direct `Entities` your organization manages. These `Entities` represent individual customers of your organization.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.entities.get_entities()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Case sensitive unique reference ID for the `Entity`.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetEntitiesRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/dinari/entities/client.py">create_entities</a>(...) -> Entity1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new `Entity` to be managed by your organization. This `Entity` represents an individual customer of your organization.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.entities.create_entities(
    name="name",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the `Entity`.

</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Case sensitive unique reference ID for the `Entity`. We recommend setting this to the unique ID of the `Entity` in your system.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/dinari/entities/client.py">get_current_entity</a>() -> Entity1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current authenticated `Entity`, which represents your organization.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.entities.get_current_entity()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/dinari/entities/client.py">get_entity_by_id</a>(...) -> Entity1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific customer `Entity` of your organization by their ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.entities.get_entity_by_id(
    entity_id="entity_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/dinari/entities/client.py">update_entity_by_id</a>(...) -> Entity1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific customer `Entity` of your organization.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.entities.update_entity_by_id(
    entity_id="entity_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Case sensitive unique reference ID for the `Entity`. We recommend setting this to the unique ID of the `Entity` in your system.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Accounts

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_entity_accounts</a>(...) -> GetEntityAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all `Accounts` that belong to a specific `Entity`. This `Entity` represents your organization itself, or an individual customer of your organization.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_entity_accounts(
    entity_id="entity_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetEntityAccountsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">create_entity_accounts</a>(...) -> Account1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new `Account` for a specific `Entity`. This `Entity` represents your organization itself, or an individual customer of your organization.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.create_entity_accounts(
    entity_id="entity_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**jurisdiction:** `typing.Optional[Jurisdiction]` — Jurisdiction of the `Account`.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_account</a>(...) -> Account1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `Account` by its ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_account(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">create_account_deactivation</a>(...) -> Account1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the `Account` to be inactive. Inactive accounts cannot be used for trading.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.create_account_deactivation(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_account_portfolio</a>(...) -> Portfolio</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the portfolio of the `Account`, excluding cash equivalents such as stablecoins.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_account_portfolio(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page number.

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The number of stocks to return per page, maximum number is 200.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_account_cash</a>(...) -> typing.List[PaymentTokenBalance]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the cash balances of the `Account`, including stablecoins and other cash equivalents.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_account_cash(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_account_interest_payments</a>(...) -> GetAccountInterestPaymentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get interest payments made to the `Account` from yield-bearing cash holdings.

Currently, the only yield-bearing stablecoin accepted by Dinari is [USD+](https://usd.dinari.com/).

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment
import datetime

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_account_interest_payments(
    account_id="account_id",
    start_date=datetime.date.fromisoformat("2023-01-15"),
    end_date=datetime.date.fromisoformat("2023-01-15"),
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date, inclusive, in US Eastern time zone. ISO 8601 format, YYYY-MM-DD.

</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date, exclusive, in US Eastern time zone. ISO 8601 format, YYYY-MM-DD.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAccountInterestPaymentsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_account_dividend_payments</a>(...) -> GetAccountDividendPaymentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get dividend payments made to the `Account` from dividend-bearing stock holdings.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment
import datetime

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_account_dividend_payments(
    account_id="account_id",
    start_date=datetime.date.fromisoformat("2023-01-15"),
    end_date=datetime.date.fromisoformat("2023-01-15"),
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date, inclusive, in US Eastern time zone. ISO 8601 format, YYYY-MM-DD.

</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date, exclusive, in US Eastern time zone. ISO 8601 format, YYYY-MM-DD.

</dd>
</dl>

<dl>
<dd>

**stock_id:** `typing.Optional[str]` — Optional ID of the `Stock` to filter by

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAccountDividendPaymentsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">create_account_faucet</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mints 1,000 mockUSD sandbox payment tokens to the `Wallet` connected to the `Account`.

This feature is only supported in sandbox mode.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.create_account_faucet(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**chain_id:** `typing.Optional[ChainId]` — CAIP-2 chain ID of blockchain in which to mint the sandbox payment tokens. If none specified, defaults to eip155:421614. If the `Account` is linked to a Dinari-managed `Wallet`, only eip155:42161 is allowed.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_brokerage_account_activities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of brokerage activities tied to the specified `Account`.

**⚠️ ALPHA: This endpoint is in early development and subject to breaking changes.**

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_brokerage_account_activities(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of entries to return in the response. Defaults to 100.

</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination token. Set to the `id` field of the last Activity returned in the previous page to get the next page of results.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_token_transfers</a>(...) -> GetTokenTransfersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get `TokenTransfer`s made from this `Account`.

A `TokenTransfer` represents a transfer of tokens through the Dinari platform from one `Account` to another.
As such, only `Account`s that are connected to Dinari-managed `Wallet`s can initiate `TokenTransfer`s.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_token_transfers(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetTokenTransfersRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">create_token_transfers</a>(...) -> TokenTransfer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `TokenTransfer` from this `Account`.

A `TokenTransfer` represents a transfer of tokens through the Dinari platform from one `Account` to another.
As such, only `Account`s that are connected to Dinari-managed `Wallet`s can initiate `TokenTransfer`s.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.create_token_transfers(
    account_id="account_id",
    recipient_account_id="recipient_account_id",
    token_address="token_address",
    quantity=1.1,
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**recipient_account_id:** `str` — ID of the recipient account to which the tokens will be transferred.

</dd>
</dl>

<dl>
<dd>

**token_address:** `str` — Address of the token to transfer.

</dd>
</dl>

<dl>
<dd>

**quantity:** `float` — Quantity of the token to transfer.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.accounts.<a href="src/dinari/accounts/client.py">get_token_transfer</a>(...) -> TokenTransfer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `TokenTransfer` made from this `Account` by its ID.

A `TokenTransfer` represents a transfer of tokens through the Dinari platform from one `Account` to another.
As such, only `Account`s that are connected to Dinari-managed `Wallet`s can initiate `TokenTransfer`s.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.accounts.get_token_transfer(
    account_id="account_id",
    transfer_id="transfer_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**transfer_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## KYC

<details><summary><code>client.kyc.<a href="src/dinari/kyc/client.py">get_entity_kyc</a>(...) -> Kyc</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get most recent KYC data of the `Entity`.

If there are any completed KYC checks, data from the most recent one will be returned.
If there are no completed KYC checks, the most recent KYC check information, regardless of status, will be returned.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.kyc.get_entity_kyc(
    entity_id="entity_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/dinari/kyc/client.py">create_entity_kyc</a>(...) -> Kyc</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit KYC data directly, for partners that are provisioned to provide their own KYC data.

This feature is available for everyone in sandbox mode, and for specifically provisioned partners in production.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari, CreateKycInput_Baseline, BaselineKycCheckDataV0
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.kyc.create_entity_kyc(
    entity_id="entity_id",
    request=CreateKycInput_Baseline(
        data=BaselineKycCheckDataV0(
            country_code="SG",
            last_name="Doe",
            address_country_code="SG",
        ),
        provider_name="provider_name",
    ),
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request:** `CreateKycInput`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/dinari/kyc/client.py">get_entity_kyc_document</a>(...) -> typing.List[KycDocument]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get uploaded documents for a KYC check

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.kyc.get_entity_kyc_document(
    entity_id="entity_id",
    kyc_id="kyc_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**kyc_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/dinari/kyc/client.py">create_entity_kyc_document</a>(...) -> KycDocument</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload KYC-related documentation for partners that are provisioned to provide their own KYC data.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.kyc.create_entity_kyc_document(
    entity_id="entity_id",
    kyc_id="kyc_id",
    document_type="GOVERNMENT_ID",
    file="example_file",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**kyc_id:** `str`

</dd>
</dl>

<dl>
<dd>

**document_type:** `KycDocumentType` — Type of `KYCDocument` to be uploaded.

</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — File to be uploaded. Must be a valid image or PDF file (jpg, jpeg, png, pdf) less than 10MB in size.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.kyc.<a href="src/dinari/kyc/client.py">create_managed_entity_kyc_embed</a>(...) -> ManagedKycEmbed</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a Dinari-managed KYC Check and get a URL for your end customer to interact with.

The URL points to a web-based KYC interface that can be presented to the end customer for KYC verification.
Once the customer completes this KYC flow, the KYC check will be created and available in the KYC API.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.kyc.create_managed_entity_kyc_embed(
    entity_id="entity_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str`

</dd>
</dl>

<dl>
<dd>

**jurisdiction:** `typing.Optional[Jurisdiction]` — Jurisdiction for the KYC check. Defaults to BASELINE.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Orders

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">get_entity_orders</a>(...) -> GetEntityOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all `Orders` under the `Entity`.<br>Optionally `Orders` can be transaction hash or fulfillment transaction hash.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.get_entity_orders()

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `typing.Optional[str]` — CAIP-2 formatted chain ID of the blockchain the `Order` was made on.

</dd>
</dl>

<dl>
<dd>

**order_transaction_hash:** `typing.Optional[str]` — Transaction hash of the `Order`.

</dd>
</dl>

<dl>
<dd>

**order_fulfillment_transaction_hash:** `typing.Optional[str]` — Fulfillment transaction hash of the `Order`.

</dd>
</dl>

<dl>
<dd>

**order_request_id:** `typing.Optional[str]` — Order Request ID for the `Order`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetEntityOrdersRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">get_orders</a>(...) -> GetOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all `Orders` under the `Account`.<br>Optionally `Orders` can be filtered by chain ID, transaction hash, or client order ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.get_orders(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**chain_id:** `typing.Optional[str]` — CAIP-2 formatted chain ID of the blockchain the `Order` was made on.

</dd>
</dl>

<dl>
<dd>

**order_transaction_hash:** `typing.Optional[str]` — Transaction hash of the `Order`.

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied identifier to search for `Order`s.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetOrdersRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">get_order_by_id</a>(...) -> Order</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `Order` by its ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.get_order_by_id(
    account_id="account_id",
    order_id="order_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">create_order_cancellation</a>(...) -> Order</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an `Order` by its ID. Note that this requires the `Order` ID, not the `OrderRequest` ID.
Once you submit a cancellation request, it cannot be undone. Be advised that orders with a
status of PENDING_FILL, PENDING_ESCROW, FILLED, REJECTED, or CANCELLED cannot be cancelled.

`Order` cancellation is not guaranteed nor is it immediate. The `Order` may still be executed
if the cancellation request is not received in time.

Check the status using the "Get Order by ID" endpoint to confirm whether the `Order` has been cancelled.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.create_order_cancellation(
    account_id="account_id",
    order_id="order_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">create_batch_order_cancellation</a>(...) -> BatchCancelOrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel multiple `Orders` by their IDs in a single request. Note that this requires the `Order` IDs, not the `OrderRequest` IDs.
Once you submit a cancellation request, it cannot be undone. Be advised that orders with a
status of PENDING_FILL, PENDING_ESCROW, FILLED, REJECTED, or CANCELLED cannot be cancelled.

`Order` cancellation is not guaranteed nor is it immediate. The `Orders` may still be executed
if the cancellation request is not received in time.

The response will indicate which orders were successfully queued to cancel and which failed to queue.
Check the status using the "Get Order by ID" endpoint to confirm whether individual `Orders` have been cancelled.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.create_batch_order_cancellation(
    account_id="account_id",
    order_ids=[
        "order_ids"
    ],
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_ids:** `typing.List[str]` — List of `Order` IDs to cancel

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">get_account_all_order_fulfillments</a>(...) -> GetAccountAllOrderFulfillmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query `OrderFulfillments` under the `Account`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.get_account_all_order_fulfillments(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of `Order` IDs to query `AccountOrderFulfillment` for.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAccountAllOrderFulfillmentsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">get_account_order_fulfillments</a>(...) -> GetAccountOrderFulfillmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get `OrderFulfillments` for a specific `Order`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.get_account_order_fulfillments(
    account_id="account_id",
    order_id="order_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAccountOrderFulfillmentsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/dinari/orders/client.py">get_account_order_fulfillment_by_id</a>(...) -> OrderFulfillment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `OrderFulfillment` by its ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.orders.get_account_order_fulfillment_by_id(
    account_id="account_id",
    order_fulfillment_id="order_fulfillment_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_fulfillment_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Wallets

<details><summary><code>client.wallets.<a href="src/dinari/wallets/client.py">get_wallet</a>(...) -> Wallet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the wallet connected to the `Account`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.wallets.get_wallet(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/dinari/wallets/client.py">get_account_wallet_connection_nonce</a>(...) -> AccountWalletConnectionMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a nonce and message to be signed in order to verify `Wallet` ownership.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.wallets.get_account_wallet_connection_nonce(
    account_id="account_id",
    wallet_address="wallet_address",
    chain_id="eip155:0",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**wallet_address:** `str` — Address of the `Wallet` to connect.

</dd>
</dl>

<dl>
<dd>

**chain_id:** `WalletChainId` — CAIP-2 formatted chain ID of the blockchain the `Wallet` is on. eip155:0 is used for EOA wallets

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/dinari/wallets/client.py">create_account_wallet_connection</a>(...) -> Wallet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect a `Wallet` to the `Account` after verifying the signature.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.wallets.create_account_wallet_connection(
    account_id="account_id",
    signature="signature",
    nonce="nonce",
    wallet_address="wallet_address",
    chain_id="eip155:0",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**signature:** `str` — Signature payload from signing the connection message with the `Wallet`.

</dd>
</dl>

<dl>
<dd>

**nonce:** `str` — Nonce contained within the connection message.

</dd>
</dl>

<dl>
<dd>

**wallet_address:** `str` — Address of the `Wallet`.

</dd>
</dl>

<dl>
<dd>

**chain_id:** `WalletChainId` — CAIP-2 formatted chain ID of the blockchain the `Wallet` to link is on. eip155:0 is used for EOA wallets

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/dinari/wallets/client.py">create_account_wallet_internal_connection</a>(...) -> Wallet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect an internal `Wallet` to the `Account`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.wallets.create_account_wallet_internal_connection(
    account_id="account_id",
    wallet_address="wallet_address",
    chain_id="eip155:0",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**wallet_address:** `str` — Address of the `Wallet`.

</dd>
</dl>

<dl>
<dd>

**chain_id:** `WalletChainId` — CAIP-2 formatted chain ID of the blockchain the `Wallet` to link is on. eip155:0 is used for EOA wallets

</dd>
</dl>

<dl>
<dd>

**is_shared:** `typing.Optional[bool]` — Is the linked Wallet shared or not

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Order Requests

<details><summary><code>client.order_requests.<a href="src/dinari/order_requests/client.py">get_list_order_requests</a>(...) -> GetListOrderRequestsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists `OrderRequests`.<br>Optionally `OrderRequests` can be filtered by certain parameters.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.order_requests.get_list_order_requests(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_request_id:** `typing.Optional[str]` — Order Request ID for the `OrderRequest`

</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` — Order ID for the `OrderRequest`

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied ID to map this `OrderRequest` to an order in their own systems.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetListOrderRequestsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.order_requests.<a href="src/dinari/order_requests/client.py">get_order_request_by_id</a>(...) -> OrderRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `OrderRequest` by its ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.order_requests.get_order_request_by_id(
    account_id="account_id",
    order_request_id="order_request_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**order_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.order_requests.<a href="src/dinari/order_requests/client.py">create_eip155order_request_permit</a>(...) -> Eip155OrderRequestPermit</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a permit that can be signed and used to create an `OrderRequest` using Dinari's EVM smart contracts.

This is a convenience method to prepare the transactions needed to create an `OrderRequest` using Dinari's EVM smart contracts.
Once signed, the transactions can be sent to the EVM network to create the order.
Note that the fee quote is already included in the transactions, so no additional fee quote lookup is needed.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.order_requests.create_eip155order_request_permit(
    account_id="account_id",
    chain_id="eip155:1",
    order_tif="DAY",
    order_side="BUY",
    order_type="MARKET",
    payment_token="payment_token",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**chain_id:** `ChainId` — CAIP-2 chain ID of the blockchain where the `Order` will be placed.

</dd>
</dl>

<dl>
<dd>

**order_tif:** `OrderTif` — Time in force. Indicates how long `Order` is valid for.

</dd>
</dl>

<dl>
<dd>

**order_side:** `OrderSide` — Indicates whether `Order` is a buy or sell.

</dd>
</dl>

<dl>
<dd>

**order_type:** `OrderType` — Type of `Order`.

</dd>
</dl>

<dl>
<dd>

**payment_token:** `str` — Address of payment token. Required for Accounts outside of US jurisdiction. Accounts with US jurisdiction must use: USDC for live, MockUSD for sandbox.

</dd>
</dl>

<dl>
<dd>

**payment_token_quantity:** `typing.Optional[float]` — Amount of payment tokens involved. Required for market buy `Orders`.

</dd>
</dl>

<dl>
<dd>

**asset_token_quantity:** `typing.Optional[float]` — Amount of dShare asset tokens involved. Required for limit `Order Requests` and market sell `Order Requests`. Must be a positive number with a precision of up to 4 decimal places for limit `Order Requests` or up to 6 decimal places for market sell `Order Requests`.

</dd>
</dl>

<dl>
<dd>

**limit_price:** `typing.Optional[float]` — Price per asset in the asset's native currency. USD for US equities and ETFs. Required for limit `Orders`.

</dd>
</dl>

<dl>
<dd>

**stock_id:** `typing.Optional[str]` — The ID of the `Stock` for which the `Order` is being placed.

</dd>
</dl>

<dl>
<dd>

**token_id:** `typing.Optional[str]` — The ID of the `Token` for which the `Order` is being placed.

</dd>
</dl>

<dl>
<dd>

**alloy_id:** `typing.Optional[str]` — The ID of the `Alloy` for which the `Order` is being placed.

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied unique identifier to map this `Order` to an order in the customer's systems.

</dd>
</dl>

<dl>
<dd>

**fee:** `typing.Optional[float]` — Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.order_requests.<a href="src/dinari/order_requests/client.py">create_eip155order_request_permit_transaction</a>(...) -> Eip155OrderRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a transaction for an EIP155 Order Request given the EIP155OrderRequest ID and Permit Signature.

An `EIP155OrderRequest` representing the proxied order is returned.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.order_requests.create_eip155order_request_permit_transaction(
    account_id="account_id",
    order_request_id="order_request_id",
    permit_signature="permit_signature",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request:** `Eip155OrderRequestPermitTransaction`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.order_requests.<a href="src/dinari/order_requests/client.py">create_eip155permit_transaction</a>(...) -> Eip155Transaction</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prepare a transaction to be placed on EVM. The returned structure contains the necessary
data to create an `EIP155Transaction` object.

Safe wallets can send `0x` as `permit_signature`. Those orders aren't simulated before they're returned.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.order_requests.create_eip155permit_transaction(
    account_id="account_id",
    order_request_id="order_request_id",
    permit_signature="permit_signature",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request:** `Eip155OrderRequestPermitTransaction`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Managed Orders

<details><summary><code>client.managed_orders.<a href="src/dinari/managed_orders/client.py">create_market_buy_managed_order_request</a>(...) -> OrderRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a managed `OrderRequest` to place a market buy `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.managed_orders.create_market_buy_managed_order_request(
    account_id="account_id",
    payment_amount=1.1,
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**payment_amount:** `float`

Amount of currency (USD for US equities and ETFs) to pay for the order.
Must be a positive number with a precision of up to 2 decimal places.

</dd>
</dl>

<dl>
<dd>

**payment_token_address:** `typing.Optional[str]` — Address of the payment token to be used for the payment of the order. If not provided, the default payment token (USD+) will be used.

</dd>
</dl>

<dl>
<dd>

**stock_id:** `typing.Optional[str]` — ID of `Stock`.

</dd>
</dl>

<dl>
<dd>

**alloy_id:** `typing.Optional[str]` — ID of `Alloy`.

</dd>
</dl>

<dl>
<dd>

**recipient_account_id:** `typing.Optional[str]` — ID of `Account` to receive the `Order`.

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

</dd>
</dl>

<dl>
<dd>

**fee:** `typing.Optional[float]` — Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.managed_orders.<a href="src/dinari/managed_orders/client.py">create_market_sell_managed_order_request</a>(...) -> OrderRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a managed `OrderRequest` to place a market sell `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.managed_orders.create_market_sell_managed_order_request(
    account_id="account_id",
    asset_quantity=1.1,
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**asset_quantity:** `float` — Quantity of shares to trade. Must be a positive number with a precision of up to 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**stock_id:** `typing.Optional[str]` — ID of `Stock`.

</dd>
</dl>

<dl>
<dd>

**alloy_id:** `typing.Optional[str]` — ID of `Alloy`.

</dd>
</dl>

<dl>
<dd>

**recipient_account_id:** `typing.Optional[str]` — ID of `Account` to receive the `Order`.

</dd>
</dl>

<dl>
<dd>

**payment_token_address:** `typing.Optional[str]` — Address of the payment token to be used for the sell order. If not provided, the default payment token (USD+) will be used. Should only be specified if `recipient_account_id` for a non-managed wallet account is also provided.

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

</dd>
</dl>

<dl>
<dd>

**fee:** `typing.Optional[float]` — Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.managed_orders.<a href="src/dinari/managed_orders/client.py">create_limit_buy_managed_order_request</a>(...) -> OrderRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a managed `OrderRequest` to place a limit buy `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.managed_orders.create_limit_buy_managed_order_request(
    account_id="account_id",
    asset_quantity=1.1,
    limit_price=1.1,
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**asset_quantity:** `float` — Amount of dShare asset involved. Required for limit `Order Requests` and market sell `Order Requests`. Must be a positive number with a precision of up to 4 decimal places.

</dd>
</dl>

<dl>
<dd>

**limit_price:** `float` — Price at which to execute the order. Must be a positive number with a precision of up to 2 decimal places.

</dd>
</dl>

<dl>
<dd>

**stock_id:** `typing.Optional[str]` — ID of `Stock`.

</dd>
</dl>

<dl>
<dd>

**alloy_id:** `typing.Optional[str]` — ID of `Alloy`.

</dd>
</dl>

<dl>
<dd>

**recipient_account_id:** `typing.Optional[str]` — ID of `Account` to receive the `Order`.

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

</dd>
</dl>

<dl>
<dd>

**payment_token_address:** `typing.Optional[str]` — Address of the payment token to be used for the payment of the order. If not provided, the default payment token (USD+) will be used.

</dd>
</dl>

<dl>
<dd>

**fee:** `typing.Optional[float]` — Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.managed_orders.<a href="src/dinari/managed_orders/client.py">create_limit_sell_managed_order_request</a>(...) -> OrderRequest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a managed `OrderRequest` to place a limit sell `Order`.

Fees for the `Order` can optionally be specified in the `OrderRequest` for DFN orders in USD, supporting up to 6 decimal places

If an `OrderRequest` with the same `client_order_id` already exists for the given account, the creation call will fail.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.managed_orders.create_limit_sell_managed_order_request(
    account_id="account_id",
    asset_quantity=1.1,
    limit_price=1.1,
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**asset_quantity:** `float` — Amount of dShare asset involved. Required for limit `Order Requests` and market sell `Order Requests`. Must be a positive number with a precision of up to 4 decimal places.

</dd>
</dl>

<dl>
<dd>

**limit_price:** `float` — Price at which to execute the order. Must be a positive number with a precision of up to 2 decimal places.

</dd>
</dl>

<dl>
<dd>

**stock_id:** `typing.Optional[str]` — ID of `Stock`.

</dd>
</dl>

<dl>
<dd>

**alloy_id:** `typing.Optional[str]` — ID of `Alloy`.

</dd>
</dl>

<dl>
<dd>

**recipient_account_id:** `typing.Optional[str]` — ID of `Account` to receive the `Order`.

</dd>
</dl>

<dl>
<dd>

**payment_token_address:** `typing.Optional[str]` — Address of the payment token to be used for the sell order. If not provided, the default payment token (USD+) will be used. Should only be specified if `recipient_account_id` for a non-managed wallet account is also provided.

</dd>
</dl>

<dl>
<dd>

**client_order_id:** `typing.Optional[str]` — Customer-supplied ID to map this order to an order in their own systems. Must be unique within the entity.

</dd>
</dl>

<dl>
<dd>

**fee:** `typing.Optional[float]` — Optional fee amount associated with `Order` in USD for DFN orders. Must be a positive number with a precision of up to 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

## Withdrawals

<details><summary><code>client.withdrawals.<a href="src/dinari/withdrawals/client.py">get_account_withdrawal_requests</a>(...) -> GetAccountWithdrawalRequestsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List `WithdrawalRequests` under the `Account`, sorted by most recent.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.withdrawals.get_account_withdrawal_requests(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAccountWithdrawalRequestsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.withdrawals.<a href="src/dinari/withdrawals/client.py">create_account_withdrawal_requests</a>(...) -> WithdrawalRequest1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request to withdraw USD+ payment tokens from a managed `Account` and send the equivalent amount of USDC to the specified recipient `Account`.

The recipient `Account` must belong to the same `Entity` as the managed `Account`.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.withdrawals.create_account_withdrawal_requests(
    account_id="account_id",
    recipient_account_id="recipient_account_id",
    payment_token_quantity=1.1,
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**recipient_account_id:** `str` — ID of the `Account` that will receive payment tokens from the `Withdrawal`.

</dd>
</dl>

<dl>
<dd>

**payment_token_quantity:** `float` — Amount of USD+ payment tokens to be withdrawn. Must be greater than 0 and have at most 6 decimal places.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.withdrawals.<a href="src/dinari/withdrawals/client.py">get_account_withdrawal_request</a>(...) -> WithdrawalRequest1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `WithdrawalRequest` by its ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.withdrawals.get_account_withdrawal_request(
    account_id="account_id",
    withdrawal_request_id="withdrawal_request_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**withdrawal_request_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.withdrawals.<a href="src/dinari/withdrawals/client.py">get_account_withdrawals</a>(...) -> GetAccountWithdrawalsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all `Withdrawals` under the `Account`, sorted by most recent.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.withdrawals.get_account_withdrawals(
    account_id="account_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**withdrawal_request_id:** `typing.Optional[str]` — ID of the `WithdrawalRequest` to find `Withdrawals` for.

</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results to return

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GetAccountWithdrawalsRequestOrder]` — Sort order

</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Cursor for next page

</dd>
</dl>

<dl>
<dd>

**previous:** `typing.Optional[str]` — Cursor for previous page

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>

<details><summary><code>client.withdrawals.<a href="src/dinari/withdrawals/client.py">get_account_withdrawal</a>(...) -> Withdrawal1</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific `Withdrawal` by its ID.

</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from dinari import Dinari
from dinari.environment import DinariEnvironment

client = Dinari(
    api_key_id="<value>",
    api_secret_key="<X-API-Secret-Key>",
    environment=DinariEnvironment.PRODUCTION,
)

client.withdrawals.get_account_withdrawal(
    account_id="account_id",
    withdrawal_id="withdrawal_id",
)

```

</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_id:** `str`

</dd>
</dl>

<dl>
<dd>

**withdrawal_id:** `str`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>

</dd>
</dl>
</details>
