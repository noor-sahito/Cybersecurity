# Hash Functions

## Overview

A hash function is a cryptographic algorithm that takes an input of arbitrary size and produces a fixed-length output called a **hash value** or **digest**.

Hash functions are **one-way functions**, meaning the original input cannot be feasibly reconstructed from the hash. They are a fundamental building block in modern cryptography and cybersecurity.

Hash functions are widely used for:
- Password storage
- Data integrity verification
- Digital signatures
- Message authentication
- Blockchain systems

---

## Key Properties of Cryptographic Hash Functions

A secure cryptographic hash function must satisfy the following properties:

### Deterministic
- The same input always produces the same hash output.

### Fixed-Length Output
- Regardless of input size, the output length is always the same.

### Pre-image Resistance
- Given a hash, it should be computationally infeasible to find the original input.

### Second Pre-image Resistance
- It should be infeasible to find a different input that produces the same hash.

### Collision Resistance
- It should be extremely difficult to find two different inputs that produce the same hash.

---

## How Hash Functions Work

1. Input data (message, file, password) is provided
2. The hash algorithm processes the input
3. A fixed-length hash value is generated
4. Even a tiny change in input results in a completely different hash

This behavior is known as the **avalanche effect**.

---

## Common Hash Algorithms

### MD5 (Message Digest 5)
- Produces a 128-bit hash
- Fast but **cryptographically broken**
- Vulnerable to collisions
- **Not secure** for modern applications

### SHA-1 (Secure Hash Algorithm 1)
- Produces a 160-bit hash
- Collision attacks demonstrated
- Deprecated and no longer recommended

### SHA-2 Family
Includes:
- SHA-256
- SHA-384
- SHA-512

Features:
- Strong collision resistance
- Widely used in TLS, HTTPS, and digital certificates
- SHA-256 is especially common

### SHA-3
- Based on Keccak algorithm
- Designed as an alternative to SHA-2
- Resistant to different attack classes

---

## Hash Functions vs Encryption

| Feature | Hash Functions | Encryption |
|------|---------------|------------|
| Reversible |  No |  Yes |
| Key Required |  No | Yes |
| Output Size | Fixed | Variable |
| Purpose | Integrity, verification | Confidentiality |

Hashing **does not encrypt data** — it transforms data irreversibly.

---

## Password Hashing

Passwords should **never** be stored in plaintext or encrypted form.

Instead:
- Passwords are hashed
- The hash is stored
- During login, the input password is hashed again and compared

### Salting
A **salt** is a random value added to the password before hashing.

Benefits:
- Prevents rainbow table attacks
- Ensures identical passwords produce different hashes

Common password hashing algorithms:
- bcrypt
- scrypt
- Argon2 (recommended)

---

## Role in TLS and HTTPS

Hash functions are used in TLS to:
- Ensure message integrity
- Generate message authentication codes (MACs)
- Support digital signatures
- Verify certificate integrity

During the TLS handshake:
- Hash functions protect handshake messages
- Ensure no tampering occurs

---

## Hash Functions and Digital Signatures

In digital signatures:
1. The message is hashed
2. The hash is signed using the sender’s private key
3. The receiver hashes the message again
4. The signature is verified using the public key

This ensures:
- Integrity
- Authenticity
- Non-repudiation

---

## Security Considerations

Weak hash functions lead to:
- Collision attacks
- Forged signatures
- Compromised passwords

Best practices:
- Avoid MD5 and SHA-1
- Use SHA-256 or stronger
- Use salted hashes for passwords
- Apply key stretching where applicable

---

## Relation to Other Cryptography Topics

- Hash functions support digital signatures
- TLS uses hashes for integrity
- MITM attacks exploit weak hash validation
- Certificate validation depends on secure hashing
- Blockchain relies heavily on cryptographic hashes

---

## Conclusion

Hash functions are a cornerstone of modern cybersecurity. While they do not provide confidentiality, they are essential for ensuring data integrity, authentication, and trust. Understanding hash functions is critical for secure system design, TLS analysis, password security, and cryptographic protocols.
