# Design Note — AutomataLab: Real-Time Input Validation

**Course:** 21CSC301T — Formal Language and Automata  
**Assessment Task 2 | B.Tech AIML | Semester V | AY 2026–2027**  
**SDG 9 — Industry, Innovation and Infrastructure**

## 1. Objective
Design finite-state recognizers for password policy, email syntax and ATM PIN format. This project includes an interactive browser demonstration and Python implementations with automated tests.

## 2. Password policy DFA
Alphabet classes: `L` lowercase ASCII, `U` uppercase ASCII, `D` digit, `S` one of `!@#$%^&*`, and `X` all other symbols. The language is:
`{w ∈ (L ∪ U ∪ D ∪ S)* | 8 ≤ |w| ≤ 20 and w contains at least one symbol from each of L,U,D,S}`.
The DFA state is compactly encoded as `(n, mask)`, where `n` is consumed length (bounded at 21) and `mask` records the four category flags. Unsupported input or length >20 rejects. Accept iff length is 8–20 and all four bits are set.

## 3. Email syntax DFA
The accepted subset requires exactly one `@`; a non-empty local part using ASCII letters, digits and `._%+-`; no leading, trailing or consecutive local dots; at least two domain labels; each label contains ASCII alphanumeric characters and internal hyphens only; final label is at least two ASCII letters. A finite-state recognizer tracks local/domain phase and dot/hyphen/separator conditions. This is intentionally a restricted grammar, not full RFC 5322.

## 4. ATM PIN DFA
Alphabet `Σ={0,1,...,9}`. Language: `L_PIN={w∈Σ* | |w|=4}`. States q0 through q4 count digits read; q0 is start and q4 is the only accepting state. A non-digit or fifth character transitions to a dead state. Leading zeroes are valid.

## 5. Test vectors

| Application | Accepted | Rejected |
|---|---|---|
| Password | `Abcdef1!`, `StrongPass9@`, `Aa1!bcde`, `Zx7#mnopQ`, `A1!bcdefghijklmnopq` | `abcdef1!`, `ABCDEFG1!`, `Abcdefgh!`, `Abcdefg1`, `Ab1!xyz` |
| Email | `alice@example.com`, `john.doe@mail.co.uk`, `a_b+c@example-domain.org`, `user123@sub.example.in`, `x@y.ab` | `@example.com`, `aliceexample.com`, `alice@@example.com`, `alice..bob@example.com`, `alice@example` |
| PIN | `1234`, `0000`, `9071`, `5555`, `0420` | `123`, `12345`, `12a4`, `12 4`, empty string |

## 6. Syntax versus semantics

| Application | Finite automaton validates | Additional processing required |
|---|---|---|
| Password | Length, allowed characters, category presence | Breached-password checks, hashing, MFA, account policy |
| Email | Basic lexical structure | DNS/MX lookup, mailbox ownership confirmation |
| PIN | Four numeric digits | PIN/account match, encrypted verification, attempt limits, fraud controls |

Finite automata are appropriate for regular languages and bounded policies. External lookups, cryptographic checks, identity and database state are outside this recognizer's role.

## 7. Complexity and comparison
All three validators scan the input once: `O(n)` time. Their control state is finite and bounded, so auxiliary state is `O(1)`. PIN has the simplest DFA (five progress states plus dead state). Password needs a bounded length plus four flags. Email requires more structural state to handle separators and labels.

## 8. Limitations and SDG 9
The password policy is an assignment example, not universal best practice. Email validation is a restricted subset and cannot prove mailbox existence. A four-digit PIN is an assumption, not a universal bank standard. None of these validators authenticates a person. The project aligns at design level with SDG 9 by illustrating predictable input validation as a building block for reliable digital services.

## 9. Five-minute demonstration
- 0:00–0:30 — Introduce finite automata and the three use cases.
- 0:30–1:30 — Password: test `StrongPass9@` and `abcdef1!`; explain length and category flags.
- 1:30–2:30 — Email: test `alice@example.com` and `alice@@example.com`; explain `@` and domain labels.
- 2:30–3:15 — PIN: test `0420` and `12345`; trace q0→q4.
- 3:15–4:15 — Run Python unit tests.
- 4:15–5:00 — Explain syntax vs semantic checks, limitations and SDG 9.

## 10. Conclusion
The implementation demonstrates that finite automata can validate bounded character policies and structured input syntax efficiently. The PIN validator is a direct counting DFA; password and email use compact finite-state scans. Production systems must add semantic and security layers.
