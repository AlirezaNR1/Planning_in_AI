# Planning_in_AI

## Introduction to Planning

Planning in artificial intelligence involves the strategic sequencing of actions to achieve a specific goal or reach a desired state from an initial condition. It involves evaluating potential actions, considering the current state, and navigating through possible transitions to achieve a defined objective efficiently.

### States and Actions in Planning

In planning, states represent the conditions of the environment or system, while actions are the operations or changes that can be applied to move from one state to another. These actions modify the current state, eventually leading to the desired goal state.

### Introduction to Planning Domains

In the context of this project, planning domains refer to distinct problem-solving areas with specific rules, states, actions, and objectives. Each domain encapsulates a unique scenario or problem to solve.

### `SpareTireDomain`

### Description

The `SpareTireDomain` represents a scenario where the initial state comprises a flat tire on the axle and a spare tire in the trunk. The objective is to execute a series of actions to replace the flat tire with the spare tire.

### States

This domain consists of:

- Tires: Spare tire and flat tire
- Locations: Ground, axle, trunk

### Actions

The series of actions to reach the final state involves:

1. Remove flat tire from axle
   - Precondition: Flat tire should be on the axle.
   - Effects: Moves the flat tire from the axle.
2. Remove spare tire from trunk
   - Precondition: Spare tire should be in the trunk.
   - Effects: Removes the spare tire from the trunk.
3. Put spare tire on axle
   - Effects: Places the spare tire onto the axle.

### Objects

- Spare tire
- Flat tire
- Locations: Ground, axle, trunk


### `BlocksWorld`

### Description

The `BlocksWorld` represents a scenario where the initial state comprises a table with three blocks called A, B, C and block C is on block A and blocks A and B are on the table. The objective is to execute a series of actions to place block A on block B and block B on block C.

![blocks](https://github.com/AlirezaNR1/Planning_in_AI/assets/141549257/abd0ceac-9926-4e32-8024-b24ade7ef6a8)

### States

This domain consists of:

- Blcoks: Block A, B, C
- Locations: On other blocks or on table

### Actions

The series of actions to reach the final state involves:

1. Move black C from A to table
   - Precondition: blcok C on Block A and table has an empty spot
   - Effects: block C is on table and block A can be moved
2. Move blcok B from table to block C
   - Precondition: nothing on block B, nothing on block C.
   - Effects: blcok B on blcok C.
3. Move block A from table to block B
   - Precondition: nothing on blcok A, nothing on block B.
   - Effects: Block A on block B.

### Objects

- Blocks A, B, C

### `DinnerDatesDomain`

### Description

The `DinnerDatesDomain` represents a scenario where the initial state comprises a house with garbage, uncooked meal and unwrapped gift. The objective is to execute a series of actions to take the trash out, cook the meal and wrap the gift.

### States

This domain consists of:

- bag of garbage
- clean hands
- quiet place

### Actions

The series of actions to reach the final state involves:

1. cook the meal:
   - Precondition: hands should be clean.
   - Effects: meal is cooked.
2. wrap the gift:
   - Precondition: it should be quiet.
   - Effects: present is ready.
3. carry the trash out
   - Effects: garbage is out and hand are not clean.

### Objects

- garbage, clean hands, quiet place


## Planning Methods

- Forward Search: A method that explores possible actions from the initial state to the goal.
- Backward Search: A method that starts from the goal state and works backward to determine actions leading from it to the initial state.
