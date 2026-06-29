terraform {
  backend "s3" {
    bucket         = "muhammad-resume-2026-fra"
    key            = "backend/terraform.tfstate"
    region         = "eu-central-1"
    # Profile removed here so GitHub Actions can read it natively using OIDC credentials!
  }
}
