resource "google_compute_backend_service" "frontend-backendservice" {
  name        = "frontend-backendservice"
  description = "Backend service managing connectivity to the frontend pods in the k8s cluster"
  timeout_sec = 10
  enable_cdn  = false
  port_name   = "frontend-port"

  backend {

    group = "${google_compute_instance_group_manager.k8sclstr-ig-manager.instance_group}"

  }
  health_checks = ["${google_compute_health_check.frontend-healthchecks.self_link}"]
}

resource "google_compute_backend_service" "backend-backendservice" {
  name        = "backend-backendservice"
  description = "Backend service managing connectivity to the backend pods in the k8s cluster"
  timeout_sec = 10
  enable_cdn  = false
  port_name   = "backend-port"

  backend {
    group = "${google_compute_instance_group_manager.k8sclstr-ig-manager.instance_group}"
  }
  health_checks = ["${google_compute_health_check.backend-healthchecks.self_link}"]
}