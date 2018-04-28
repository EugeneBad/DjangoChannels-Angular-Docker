resource "google_compute_health_check" "frontend-healthchecks" {
  name = "frontend-healthchecks"
  description = "Healthchecking the frontend pods on the k8s cluster minions"
  timeout_sec        = 1
  check_interval_sec = 1

  tcp_health_check {
    port = "30002"
  }
}

resource "google_compute_health_check" "backend-healthchecks" {
  name = "backend-healthchecks"
  description = "Healthchecking the backend pods on the k8s cluster minions"
  timeout_sec        = 1
  check_interval_sec = 1

  tcp_health_check {
    port = "30003"
  }
}