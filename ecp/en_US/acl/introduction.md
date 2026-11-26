# Access Control

ECP access control serves as a vital mechanism for restricting and managing the access privileges of different users or roles within the ECP platform. Its primary purpose is to ensure the security of data and services associated with EMQX products.  



This chapter elaborates on the following topics: 

1. [Login Authentication](./ecp_login.md) explains how to sign in to ECP with an email address and password.
2. [Single Sign-On](./sso.md) shows how to set up OIDC with Okta and sign in to ECP with a company account.
3. [Two-Factor Authentication (TOTP)](./totp_mfa.md): This section explains how to enable authenticator-app MFA for local accounts, and how to bind, sign in daily, use recovery codes, reset MFA as an admin, and perform emergency reset on the host.
4. [Authorization](./authorize.md): This section delves into the configuration of roles and permissions within the ECP.
5. [Users Management](../system_admin/user_management.md): ECP implements RBAC (Role-Based Access Control) for access control. This section introduces how system admin can perform user management-related tasks such as creating users and resetting passwords, and monitor user access and activities for platform stability and security.

Furthermore, ECP also includes an [audit logging](../system_admin/operation_audit.md) feature that records and analyzes user activities and access patterns. This facilitates the prompt identification and resolution of any anomalous behavior, thereby bolstering the overall security of EMQX products.
