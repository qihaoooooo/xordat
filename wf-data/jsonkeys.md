## Warframe Items JSON Keys

### General

| JSON Key    | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| uniqueName  | In-game ID                                                   |
| name        | In-game Display Name                                         |
| description | Flavour text                                                 |
| type        | Item type                                                    |
| imageName   | Filename of image <br />(from warframe-items CDN)            |
| category    | Similar to type<br />(E.g. for mods, indicates shotgun/warframe/etc.) |
| tradable    |                                                              |
| patchlogs   | Related patch log notes                                      |
| drops       | Possible drop locations and chances                          |
| marketCost  | Cost in platinum on the market                               |
| vaulted     |                                                              |

### Craftables

| JSON Key           | Description                       |
| ------------------ | --------------------------------- |
| buildPrice         | Cost of crafting in credits       |
| buildTime          | Crafting time                     |
| skipBuildTimePrice | Cost in platinum to rush building |
| buildQuantity      | Number of items per craft         |
| consumeOnBuild     | Reusability of blueprint          |
| components         | Required components for crafting  |

### Mods

| JSON Key    | Description                |
| ----------- | -------------------------- |
| polarity    |                            |
| rarity      |                            |
| baseDrain   | Energy drain when unranked |
| fusionLimit | Number of fusion ranks     |

### Weapons

| JSON Keys          | Description        |
| ------------------ | ------------------ |
| secondsPerShot     |                    |
| damagePerShot      |                    |
| magazineSize       |                    |
| reloadTime         |                    |
| totalDamage        |                    |
| damagePerSecond    |                    |
| trigger            |                    |
| accuracy           |                    |
| criticalChance     |                    |
| criticalMultiplier |                    |
| procChance         |                    |
| fireRate           |                    |
| chargeAttack       |                    |
| spinAttack         |                    |
| leapAttack         |                    |
| wallAttack         |                    |
| slot               |                    |
| noise              |                    |
| sentinel           | Is sentinel weapon |
| masteryReq         |                    |
| omegaAttenutation  |                    |
| channeling         |                    |
| damage             |                    |
| damageTypes        |                    |
| polarities         |                    |
| stancePolarity     |                    |
| disposition        | Riven disposition  |

### Pets

| JSON Keys | Description |
| --------- | ----------- |
| health    |             |
| shield    |             |
| armor     |             |
| stamina   |             |
| power     |             |
