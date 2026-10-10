/**
 * AgriIntel — Frontend Application Logic
 * Full-stack agricultural intelligence, neural diagnosis, and SerpApi research explorer.
 */

"use strict";

// =============================================================================
// API CONFIGURATION
// =============================================================================

// Use relative API paths if hosted on same origin; fallback to localhost:5000 for file://
const BASE_API = window.location.origin.startsWith("http")
    ? window.location.origin
    : "http://127.0.0.1:5000";

const API = {
    HEALTH: `${BASE_API}/api/health`,
    CLASSES: `${BASE_API}/api/classes`,
    DIAGNOSE: `${BASE_API}/api/diagnose`,
    SEARCH: `${BASE_API}/api/agricultural-search`
};

const MAX_IMAGE_SIZE = 15 * 1024 * 1024; // 15 MB
const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp"];

// Sample Presets Mapping
const SAMPLES = {
    tomato: {
        file: "samples/tomato_early_blight.jpg",
        name: "tomato_early_blight.jpg",
        crop: "Tomato",
        hint: "Tomato"
    },
    paddy: {
        file: "samples/paddy_bacterial_blight.jpg",
        name: "paddy_bacterial_blight.jpg",
        crop: "Paddy",
        hint: "Paddy"
    },
    wheat: {
        file: "samples/wheat_yellow_rust.jpg",
        name: "wheat_yellow_rust.jpg",
        crop: "Wheat",
        hint: "Wheat"
    },
    apple: {
        file: "samples/apple_healthy.jpg",
        name: "apple_healthy.jpg",
        crop: "Apple",
        hint: "Apple"
    }
};

// =============================================================================
// MULTILINGUAL LOCALIZATION (English, Hindi, Odia)
// =============================================================================

const I18N = {
    en: {
        brandSubtitle: "v5.0 • 87 Classes",
        heroBadge: "AI-POWERED AGRICULTURAL INTELLIGENCE",
        heroTitle: "Understand Your Crop.",
        heroTitleHighlight: "Protect Your Harvest.",
        heroSubtitle: "Upload a high-resolution leaf photograph to detect crop conditions across 87 trained classes and 22 crops. Get instant statistical predictions, verified botanical symptoms, next-step recommendations, and live agricultural extension research.",
        startDiagnosis: "🌿 Start Crop Diagnosis",
        exploreLibrary: "📚 Browse 87 Disease Classes",
        dropzonePrompt: "Drag & Drop Leaf Photo Here",
        dropzoneSubtext: "or browse from your device (JPG, PNG, WebP up to 15MB)",
        choosePhoto: "📁 Choose Photo",
        useCamera: "📷 Use Camera",
        analyzeLeaf: "🔍 Analyze Leaf",
        analyzing: "Analyzing...",
        clearPhoto: "🗑️ Clear Photo",
        predictedCrop: "Predicted Crop",
        detectedCondition: "Detected Condition",
        confidence: "Model Confidence",
        listen: "🔊 Listen to Diagnosis",
        stopAudio: "⏹️ Stop Audio",
        analyzeAnother: "📷 Analyze Another Image",
        searchHeader: "Agricultural Intelligence & Extension Sources",
        searchPrompt: "Search Agricultural Intelligence"
    },
    hi: {
        brandSubtitle: "संस्करण 5.0 • 87 श्रेणियां",
        heroBadge: "एआई-संचालित कृषि आसूचना",
        heroTitle: "अपनी फसल को समझें।",
        heroTitleHighlight: "अपनी उपज की रक्षा करें।",
        heroSubtitle: "87 प्रशिक्षित श्रेणियों एवं 22 फसलों में फसल की स्थिति पहचानने के लिए पत्ती की स्पष्ट तस्वीर अपलोड करें। तुरंत सांख्यिकीय भविष्यवाणी, सत्यापित वानस्पतिक लक्षण, अगले कदम और कृषि अनुसंधान प्राप्त करें।",
        startDiagnosis: "🌿 फसल रोग पहचान शुरू करें",
        exploreLibrary: "📚 87 रोग पुस्तकालय देखें",
        dropzonePrompt: "पत्ती की तस्वीर यहां खींचें और छोड़ें",
        dropzoneSubtext: "या अपने डिवाइस से चुनें (JPG, PNG, WebP अधिकतम 15MB)",
        choosePhoto: "📁 तस्वीर चुनें",
        useCamera: "📷 कैमरा खोलें",
        analyzeLeaf: "🔍 पत्ती का विश्लेषण करें",
        analyzing: "विश्लेषण जारी है...",
        clearPhoto: "🗑️ तस्वीर हटाएं",
        predictedCrop: "पहचानी गई फसल",
        detectedCondition: "पहचाना गया रोग / स्थिति",
        confidence: "एआई विश्वसनीयता",
        listen: "🔊 परिणाम सुनें",
        stopAudio: "⏹️ आवाज़ रोकें",
        analyzeAnother: "📷 दूसरी तस्वीर जांचें",
        searchHeader: "कृषि विश्वविद्यालय एवं अनुसंधान संदर्भ",
        searchPrompt: "कृषि संदर्भ खोजें"
    },
    or: {
        brandSubtitle: "ସଂସ୍କରଣ 5.0 • 87 ବର୍ଗ",
        heroBadge: "AI-ସଞ୍ଚାଳିତ କୃଷି ବୁଦ୍ଧିମତା",
        heroTitle: "ନିଜ ଫସଲକୁ ବୁଝନ୍ତୁ।",
        heroTitleHighlight: "ନିଜ ଅମଳକୁ ସୁରକ୍ଷିତ ରଖନ୍ତୁ।",
        heroSubtitle: "୮୭ଟି ପ୍ରଶିକ୍ଷିତ ବର୍ଗ ଏବଂ ୨୨ଟି ଫସଲରେ ରୋଗ ଚିହ୍ନଟ କରିବା ପାଇଁ ପତ୍ରର ସ୍ପଷ୍ଟ ଛବି ଅପଲୋଡ କରନ୍ତୁ। ତୁରନ୍ତ ପୂର୍ବାନୁମାନ, ଲକ୍ଷଣ ଏବଂ ପରିଚାଳନା ପରାମର୍ଶ ପାଆନ୍ତୁ।",
        startDiagnosis: "🌿 ରୋଗ ଚିହ୍ନଟ ଆରମ୍ଭ କରନ୍ତୁ",
        exploreLibrary: "📚 ୮୭ଟି ରୋଗ ତାଲିକା ଦେଖନ୍ତୁ",
        dropzonePrompt: "ପତ୍ରର ଛବି ଏଠାରେ ଛାଡ଼ନ୍ତୁ",
        dropzoneSubtext: "କିମ୍ବା ଡିଭାଇସରୁ ବାଛନ୍ତୁ (JPG, PNG, WebP ସର୍ବାଧିକ 15MB)",
        choosePhoto: "📁 ଛବି ବାଛନ୍ତୁ",
        useCamera: "📷 କ୍ୟାମେରା ବ୍ୟବହାର କରନ୍ତୁ",
        analyzeLeaf: "🔍 ପତ୍ର ବିଶ୍ଳେଷଣ କରନ୍ତୁ",
        analyzing: "ବିଶ୍ଳେଷଣ ଚାଲିଛି...",
        clearPhoto: "🗑️ ଛବି ହଟାନ୍ତୁ",
        predictedCrop: "ଚିହ୍ନଟ ହୋଇଥିବା ଫସଲ",
        detectedCondition: "ଚିହ୍ନଟ ରୋଗ / ଅବସ୍ଥା",
        confidence: "AI ବିଶ୍ୱସନୀୟତା",
        listen: "🔊 ଫଳାଫଳ ଶୁଣନ୍ତୁ",
        stopAudio: "⏹️ ଶବ୍ଦ ବନ୍ଦ କରନ୍ତୁ",
        analyzeAnother: "📷 ଅନ୍ୟ ଛବି ଯାଞ୍ଚ କରନ୍ତୁ",
        searchHeader: "କୃଷି ବିଶ୍ୱବିଦ୍ୟାଳୟ ଓ ଅନୁସନ୍ଧାନ ତଥ୍ୟ",
        searchPrompt: "କୃଷି ସୂଚନା ଖୋଜନ୍ତୁ"
    }
};

// =============================================================================
// STATE
// =============================================================================

let currentLanguage = "en";
let selectedFile = null;
let currentPreviewUrl = null;
let currentResultUrl = null;
let classesCatalog = [];
let isSpeaking = false;

// =============================================================================
// DOM REFERENCES
// =============================================================================

const DOM = {
    // Nav & System
    langSelect: document.getElementById("languageSelect"),
    statusDot: document.getElementById("statusDot"),
    statusText: document.getElementById("statusText"),
    aboutGpuValue: document.getElementById("aboutGpuValue"),

    // Studio & Upload
    dropzone: document.getElementById("dropzone"),
    dropzoneEmpty: document.getElementById("dropzoneEmpty"),
    imageInput: document.getElementById("imageInput"),
    browseFileBtn: document.getElementById("browseFileBtn"),
    cameraSnapBtn: document.getElementById("cameraSnapBtn"),
    cropHintSelect: document.getElementById("cropHintSelect"),
    previewContainer: document.getElementById("previewContainer"),
    previewImage: document.getElementById("previewImage"),
    previewDimensions: document.getElementById("previewDimensions"),
    previewSize: document.getElementById("previewSize"),
    removeImageBtn: document.getElementById("removeImageBtn"),
    analyzeImageBtn: document.getElementById("analyzeImageBtn"),
    uploadErrorAlert: document.getElementById("uploadErrorAlert"),
    uploadErrorText: document.getElementById("uploadErrorText"),

    // Loading & Error States
    loadingSection: document.getElementById("loadingSection"),
    loadingStepText: document.getElementById("loadingStepText"),
    errorSection: document.getElementById("errorSection"),
    errorDescriptionText: document.getElementById("errorDescriptionText"),
    retryAnalysisBtn: document.getElementById("retryAnalysisBtn"),

    // Results Dashboard
    resultSection: document.getElementById("resultSection"),
    imageWarningAlert: document.getElementById("imageWarningAlert"),
    imageWarningText: document.getElementById("imageWarningText"),
    rejectionAlert: document.getElementById("rejectionAlert"),
    rejectionBodyText: document.getElementById("rejectionBodyText"),
    resultImage: document.getElementById("resultImage"),
    cropResultName: document.getElementById("cropResultName"),
    conditionStatusBadge: document.getElementById("conditionStatusBadge"),
    conditionStatusIcon: document.getElementById("conditionStatusIcon"),
    conditionStatusText: document.getElementById("conditionStatusText"),
    diseaseResultName: document.getElementById("diseaseResultName"),
    pathogenName: document.getElementById("pathogenName"),
    confidencePercent: document.getElementById("confidencePercent"),
    confidenceTierPill: document.getElementById("confidenceTierPill"),
    confidenceMeterFill: document.getElementById("confidenceMeterFill"),
    confidenceMeterTrack: document.getElementById("confidenceMeterTrack"),
    topPredictionsGrid: document.getElementById("topPredictionsGrid"),
    speakResultBtn: document.getElementById("speakResultBtn"),
    speakBtnText: document.getElementById("speakBtnText"),
    newDiagnosisBtn: document.getElementById("newDiagnosisBtn"),

    // Guidance Tabs
    tabBtns: document.querySelectorAll(".tab-btn"),
    tabPanels: document.querySelectorAll(".tab-panel"),
    symptomsList: document.getElementById("symptomsList"),
    nextStepsList: document.getElementById("nextStepsList"),
    preventionList: document.getElementById("preventionList"),
    descriptionText: document.getElementById("descriptionText"),
    preliminaryWarningText: document.getElementById("preliminaryWarningText"),

    // Sources List
    diagnosisSourcesList: document.getElementById("diagnosisSourcesList"),
    refreshSourcesBtn: document.getElementById("refreshSourcesBtn"),

    // Knowledge Base Catalog
    catalogSearchInput: document.getElementById("catalogSearchInput"),
    catalogCropChips: document.getElementById("catalogCropChips"),
    catalogGrid: document.getElementById("catalogGrid"),

    // Agricultural Intel Search Form
    intelSearchForm: document.getElementById("intelSearchForm"),
    intelCropInput: document.getElementById("intelCropInput"),
    intelDiseaseInput: document.getElementById("intelDiseaseInput"),
    intelCategorySelect: document.getElementById("intelCategorySelect"),
    intelCustomQuery: document.getElementById("intelCustomQuery"),
    intelSubmitBtn: document.getElementById("intelSubmitBtn"),
    intelStatusBar: document.getElementById("intelStatusBar"),
    intelStatusCount: document.getElementById("intelStatusCount"),
    intelResultsGrid: document.getElementById("intelResultsGrid")
};

// =============================================================================
// INITIALIZATION
// =============================================================================

document.addEventListener("DOMContentLoaded", () => {
    initNavigation();
    initHealthCheck();
    initUploadHandlers();
    initSampleButtons();
    initGuidanceTabs();
    initSpeechSynthesis();
    initKnowledgeBase();
    initIntelSearch();
    initLanguageSwitcher();
});

// Navigation smooth scrolling & active indicator
function initNavigation() {
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll("main section");

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute("id");
            }
        });

        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href") === `#${current}`) {
                link.classList.add("active");
            }
        });
    });
}

// Check backend health & GPU configuration
async function initHealthCheck() {
    try {
        const response = await fetch(API.HEALTH);
        if (!response.ok) throw new Error("Health check returned status " + response.status);
        const data = await response.json();

        if (data.success && data.model_loaded) {
            if (DOM.statusDot) DOM.statusDot.className = "status-dot online";
            const deviceLabel = data.cuda_available ? (data.device_name || "CUDA GPU") : "CPU";
            if (DOM.statusText) DOM.statusText.textContent = `Online • ${deviceLabel}`;
            if (DOM.aboutGpuValue) {
                DOM.aboutGpuValue.textContent = `${data.device_name} (${data.device})`;
            }
        } else {
            if (DOM.statusDot) DOM.statusDot.className = "status-dot offline";
            if (DOM.statusText) DOM.statusText.textContent = "Model Error";
        }
    } catch (err) {
        console.warn("AgriIntel backend unreachable:", err);
        if (DOM.statusDot) DOM.statusDot.className = "status-dot offline";
        if (DOM.statusText) DOM.statusText.textContent = "Offline / Server Disconnected";
    }
}

// =============================================================================
// IMAGE UPLOAD & DROPZONE HANDLING
// =============================================================================

function initUploadHandlers() {
    // Browse File Button
    if (DOM.browseFileBtn && DOM.imageInput) {
        DOM.browseFileBtn.addEventListener("click", () => {
            DOM.imageInput.removeAttribute("capture");
            DOM.imageInput.click();
        });
    }

    // Camera Snap Button
    if (DOM.cameraSnapBtn && DOM.imageInput) {
        DOM.cameraSnapBtn.addEventListener("click", () => {
            DOM.imageInput.setAttribute("capture", "environment");
            DOM.imageInput.click();
        });
    }

    // File Input change
    if (DOM.imageInput) {
        DOM.imageInput.addEventListener("change", (e) => {
            const file = e.target.files?.[0];
            if (file) handleImageFile(file);
        });
    }

    // Drag and Drop
    if (DOM.dropzone) {
        ["dragenter", "dragover"].forEach(eventName => {
            DOM.dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                DOM.dropzone.classList.add("drag-active");
            }, false);
        });

        ["dragleave", "drop"].forEach(eventName => {
            DOM.dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                DOM.dropzone.classList.remove("drag-active");
            }, false);
        });

        DOM.dropzone.addEventListener("drop", (e) => {
            const dt = e.dataTransfer;
            const file = dt.files?.[0];
            if (file) handleImageFile(file);
        });
    }

    // Remove Image Button
    if (DOM.removeImageBtn) {
        DOM.removeImageBtn.addEventListener("click", resetUploadState);
    }

    // Analyze Button
    if (DOM.analyzeImageBtn) {
        DOM.analyzeImageBtn.addEventListener("click", runCropDiagnosis);
    }

    // Retry Button
    if (DOM.retryAnalysisBtn) {
        DOM.retryAnalysisBtn.addEventListener("click", runCropDiagnosis);
    }

    // Analyze Another Image (in results)
    if (DOM.newDiagnosisBtn) {
        DOM.newDiagnosisBtn.addEventListener("click", () => {
            resetUploadState();
            document.getElementById("diagnosisSection")?.scrollIntoView({ behavior: "smooth" });
        });
    }
}

// Validate file and load preview
function handleImageFile(file) {
    hideUploadError();

    // Type validation
    if (!ALLOWED_TYPES.includes(file.type)) {
        showUploadError("Unsupported format. Please select a valid JPG, PNG, or WebP photo.");
        return;
    }

    // Size validation
    if (file.size > MAX_IMAGE_SIZE) {
        showUploadError("File is too large. Image must be under 15 MB.");
        return;
    }

    if (file.size === 0) {
        showUploadError("The selected file is empty.");
        return;
    }

    selectedFile = file;

    // Revoke previous URL
    if (currentPreviewUrl) URL.revokeObjectURL(currentPreviewUrl);
    currentPreviewUrl = URL.createObjectURL(file);

    // Update Preview in DOM
    DOM.previewImage.src = currentPreviewUrl;
    DOM.dropzoneEmpty.classList.add("hidden");
    DOM.previewContainer.classList.remove("hidden");
    DOM.removeImageBtn.classList.remove("hidden");
    DOM.analyzeImageBtn.disabled = false;

    // Read Dimensions & Size
    const imgObj = new Image();
    imgObj.onload = () => {
        DOM.previewDimensions.textContent = `Resolution: ${imgObj.width} × ${imgObj.height} px`;
        const sizeMb = (file.size / (1024 * 1024)).toFixed(2);
        DOM.previewSize.textContent = `Size: ${sizeMb} MB`;
    };
    imgObj.src = currentPreviewUrl;

    // Hide results & errors while selecting new photo
    DOM.resultSection.classList.add("hidden");
    DOM.errorSection.classList.add("hidden");
}

function resetUploadState() {
    selectedFile = null;
    if (DOM.imageInput) DOM.imageInput.value = "";
    if (currentPreviewUrl) {
        URL.revokeObjectURL(currentPreviewUrl);
        currentPreviewUrl = null;
    }

    DOM.previewImage.src = "";
    DOM.previewContainer.classList.add("hidden");
    DOM.dropzoneEmpty.classList.remove("hidden");
    DOM.removeImageBtn.classList.add("hidden");
    DOM.analyzeImageBtn.disabled = true;
    DOM.resultSection.classList.add("hidden");
    DOM.errorSection.classList.add("hidden");
    hideUploadError();
}

function showUploadError(msg) {
    if (DOM.uploadErrorAlert && DOM.uploadErrorText) {
        DOM.uploadErrorText.textContent = msg;
        DOM.uploadErrorAlert.classList.remove("hidden");
    } else {
        alert(msg);
    }
}

function hideUploadError() {
    if (DOM.uploadErrorAlert) {
        DOM.uploadErrorAlert.classList.add("hidden");
    }
}

// Sample Preset Buttons
function initSampleButtons() {
    const sampleChips = document.querySelectorAll(".sample-chip");
    sampleChips.forEach(chip => {
        chip.addEventListener("click", async () => {
            const sampleKey = chip.getAttribute("data-sample");
            const sample = SAMPLES[sampleKey];
            if (!sample) return;

            try {
                // Fetch sample image from local static directory
                const res = await fetch(sample.file);
                if (!res.ok) throw new Error("Could not load sample file: " + sample.file);
                const blob = await res.blob();
                const file = new File([blob], sample.name, { type: blob.type || "image/jpeg" });
                
                // Select matching crop hint if available
                if (DOM.cropHintSelect && sample.hint) {
                    DOM.cropHintSelect.value = sample.hint;
                }

                handleImageFile(file);
                // Smooth scroll to studio
                DOM.dropzone.scrollIntoView({ behavior: "smooth", block: "center" });
            } catch (err) {
                console.error("Failed to load sample:", err);
                showUploadError("Failed to load sample leaf image. Please choose a photo from your device.");
            }
        });
    });
}

// =============================================================================
// DIAGNOSIS INFERENCE EXECUTION
// =============================================================================

async function runCropDiagnosis() {
    if (!selectedFile) {
        showUploadError("Please select or take a leaf photo first.");
        return;
    }

    // UI state transitions
    hideUploadError();
    DOM.errorSection.classList.add("hidden");
    DOM.resultSection.classList.add("hidden");
    DOM.loadingSection.classList.remove("hidden");
    DOM.analyzeImageBtn.disabled = true;
    DOM.analyzeImageBtn.textContent = I18N[currentLanguage].analyzing;

    DOM.loadingSection.scrollIntoView({ behavior: "smooth", block: "center" });

    // Step progression animation
    const steps = [
        "Pre-processing leaf image for neural tensor...",
        "Running YOLO classification on RTX 3050 GPU...",
        "Computing Top-3 probability distributions...",
        "Validating crop boundaries & uncertainty safeguard...",
        "Retrieving verified botanical guidance & research..."
    ];
    let stepIdx = 0;
    const stepInterval = setInterval(() => {
        stepIdx = (stepIdx + 1) % steps.length;
        DOM.loadingStepText.textContent = steps[stepIdx];
    }, 700);

    const formData = new FormData();
    formData.append("image", selectedFile);
    formData.append("crop_hint", DOM.cropHintSelect ? DOM.cropHintSelect.value : "");
    formData.append("include_search", "true");

    try {
        const response = await fetch(API.DIAGNOSE, {
            method: "POST",
            body: formData
        });

        clearInterval(stepInterval);
        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.error || "Unable to complete image analysis.");
        }

        // Render diagnosis results
        renderDiagnosisResults(data);

        DOM.loadingSection.classList.add("hidden");
        DOM.resultSection.classList.remove("hidden");
        DOM.resultSection.scrollIntoView({ behavior: "smooth", block: "start" });

    } catch (err) {
        clearInterval(stepInterval);
        console.error("Diagnosis failure:", err);
        DOM.loadingSection.classList.add("hidden");
        DOM.errorSection.classList.remove("hidden");
        DOM.errorDescriptionText.textContent = err.message || "An error occurred during neural inference.";
        DOM.errorSection.scrollIntoView({ behavior: "smooth", block: "center" });
    } finally {
        DOM.analyzeImageBtn.disabled = false;
        DOM.analyzeImageBtn.textContent = I18N[currentLanguage].analyzeLeaf;
    }
}

// Render diagnosis data onto Result DOM
function renderDiagnosisResults(data) {
    const pred = data.prediction || {};
    const info = data.information || {};
    const uncertainty = data.uncertainty || {};

    // 1. Result Image
    if (currentResultUrl) URL.revokeObjectURL(currentResultUrl);
    currentResultUrl = URL.createObjectURL(selectedFile);
    DOM.resultImage.src = currentResultUrl;

    // 2. Primary Crop & Condition
    DOM.cropResultName.textContent = pred.crop_display || pred.crop || "Unknown Crop";
    DOM.diseaseResultName.textContent = pred.condition_display || pred.condition || "Unknown Condition";
    DOM.pathogenName.textContent = info.pathogen ? `Pathogen: ${info.pathogen}` : "Pathogen: Not specified";

    // 3. Health Status Badge
    const isHealthy = info.is_healthy || false;
    if (isHealthy) {
        DOM.conditionStatusBadge.className = "health-badge healthy";
        DOM.conditionStatusIcon.textContent = "🌿";
        DOM.conditionStatusText.textContent = "Healthy Foliage";
    } else {
        DOM.conditionStatusBadge.className = "health-badge";
        DOM.conditionStatusIcon.textContent = "🦠";
        DOM.conditionStatusText.textContent = info.severity || "Condition Detected";
    }

    // 4. Confidence Meter
    const confVal = Number(pred.confidence) || 0;
    DOM.confidencePercent.textContent = `${confVal.toFixed(1)}%`;
    DOM.confidenceMeterFill.style.width = `${Math.min(100, Math.max(0, confVal))}%`;

    const confLevel = pred.confidence_level || "medium";
    DOM.confidenceTierPill.className = `confidence-tier-pill ${confLevel}`;
    DOM.confidenceTierPill.textContent = confLevel.toUpperCase();

    // 5. Image Warning (Resolution / blur)
    if (data.image_warning) {
        DOM.imageWarningText.textContent = data.image_warning;
        DOM.imageWarningAlert.classList.remove("hidden");
    } else {
        DOM.imageWarningAlert.classList.add("hidden");
    }

    // 6. Uncertainty & Rejection Notice
    if (uncertainty.is_uncertain) {
        DOM.rejectionAlert.classList.remove("hidden");
        DOM.rejectionBodyText.textContent = uncertainty.rejection_message || 
            "This image may belong to a crop or condition outside the model's 16 supported classes. Please upload a clearer leaf image or consult a local agricultural expert.";
    } else {
        DOM.rejectionAlert.classList.add("hidden");
    }

    // 7. Top-3 Predictions Distribution
    renderTopPredictions(data.top_predictions || []);

    // 8. Structured Guidance Tabs
    renderGuidanceData(info);

    // 9. Advisory Warning
    if (data.disclaimer) {
        DOM.preliminaryWarningText.textContent = data.disclaimer;
    }

    // 10. Integrated Sources (SerpApi)
    renderExtensionSources(data.agricultural_sources || []);

    // Auto update intel search inputs for convenience
    if (DOM.intelCropInput) DOM.intelCropInput.value = pred.crop_display || "";
    if (DOM.intelDiseaseInput) DOM.intelDiseaseInput.value = pred.condition_display || "";
}

// Render Top-3 Predictions Cards
function renderTopPredictions(predictions) {
    if (!DOM.topPredictionsGrid) return;
    DOM.topPredictionsGrid.innerHTML = "";

    predictions.forEach((cand, idx) => {
        const card = document.createElement("div");
        card.className = "top-cand-card";

        const score = Number(cand.confidence) || 0;
        card.innerHTML = `
            <div class="top-cand-rank">Candidate #${idx + 1}</div>
            <div class="top-cand-name">${cand.crop_display} — ${cand.condition_display}</div>
            <div class="top-cand-bar-track">
                <div class="top-cand-bar-fill" style="width: ${Math.min(100, score)}%"></div>
            </div>
            <div class="top-cand-score">${score.toFixed(1)}% Confidence (${cand.confidence_level})</div>
        `;
        DOM.topPredictionsGrid.appendChild(card);
    });
}

// Populate Guidance Tabs (Symptoms, Next Steps, Prevention, Description)
function renderGuidanceData(info) {
    // Symptoms
    if (DOM.symptomsList) {
        DOM.symptomsList.innerHTML = "";
        const symptoms = Array.isArray(info.symptoms) ? info.symptoms : [info.symptoms || "Guidance not available."];
        symptoms.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            DOM.symptomsList.appendChild(li);
        });
    }

    // Next Steps
    if (DOM.nextStepsList) {
        DOM.nextStepsList.innerHTML = "";
        const steps = Array.isArray(info.recommended_next_steps) 
            ? info.recommended_next_steps 
            : [info.management || "Consult a local agricultural expert."];
        steps.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            DOM.nextStepsList.appendChild(li);
        });
    }

    // Prevention
    if (DOM.preventionList) {
        DOM.preventionList.innerHTML = "";
        const prev = Array.isArray(info.preventive_practices) 
            ? info.preventive_practices 
            : ["Follow clean sanitation and balanced fertilization."];
        prev.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            DOM.preventionList.appendChild(li);
        });
    }

    // Description
    if (DOM.descriptionText) {
        DOM.descriptionText.textContent = info.description || "Botanical overview is not available for this condition yet.";
    }
}

// Render SerpApi Extension Sources inside Diagnosis Result
function renderExtensionSources(sources) {
    if (!DOM.diagnosisSourcesList) return;
    DOM.diagnosisSourcesList.innerHTML = "";

    if (!sources || sources.length === 0) {
        DOM.diagnosisSourcesList.innerHTML = `
            <p class="sources-empty-state">
                No active web sources returned. Use the Agricultural Intelligence section below for custom extension queries.
            </p>
        `;
        return;
    }

    sources.forEach(src => {
        const item = document.createElement("article");
        item.className = "source-item";
        item.innerHTML = `
            <div class="source-badge-row">
                <span class="source-trust-badge">${src.trust_badge || "Agricultural Reference"}</span>
                <span class="source-domain-pill">🌐 ${src.domain || "Reference"}</span>
            </div>
            <h5 class="source-title">${escapeHtml(src.title || "Untitled Agricultural Resource")}</h5>
            <p class="source-snippet">${escapeHtml(src.snippet || "Review full page for extension notes.")}</p>
            <a href="${src.link}" target="_blank" rel="noopener noreferrer" class="source-link">
                Read Publication on ${escapeHtml(src.domain || "Source")} ↗
            </a>
        `;
        DOM.diagnosisSourcesList.appendChild(item);
    });
}

// Setup Guidance Tab Switching
function initGuidanceTabs() {
    DOM.tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const targetId = btn.getAttribute("data-tab");
            
            DOM.tabBtns.forEach(b => b.classList.remove("active"));
            DOM.tabPanels.forEach(p => p.classList.remove("active"));

            btn.classList.add("active");
            document.getElementById(targetId)?.classList.add("active");
        });
    });
}

// =============================================================================
// SPEECH SYNTHESIS (VOICE GUIDANCE IN EN, HI, OR)
// =============================================================================

function initSpeechSynthesis() {
    if (!DOM.speakResultBtn) return;

    DOM.speakResultBtn.addEventListener("click", () => {
        if (!("speechSynthesis" in window)) {
            alert("Speech output is not supported by your current browser.");
            return;
        }

        if (isSpeaking) {
            window.speechSynthesis.cancel();
            isSpeaking = false;
            DOM.speakBtnText.textContent = I18N[currentLanguage].listen;
            return;
        }

        const crop = DOM.cropResultName.textContent;
        const condition = DOM.diseaseResultName.textContent;
        const confidence = DOM.confidencePercent.textContent;

        // Gather first symptom & first next step for spoken summary
        const firstSymptom = DOM.symptomsList?.querySelector("li")?.textContent || "";
        const firstAction = DOM.nextStepsList?.querySelector("li")?.textContent || "";

        let speechText = "";
        if (currentLanguage === "hi") {
            speechText = `फसल पहचान परिणाम। फसल: ${crop}। स्थिति: ${condition}। एआई विश्वसनीयता: ${confidence}। अगला कदम: ${firstAction}।`;
        } else if (currentLanguage === "or") {
            speechText = `ଫସଲ ଚିହ୍ନଟ ଫଳାଫଳ। ଫସଲ: ${crop}। ଅବସ୍ଥା: ${condition}। ବିଶ୍ୱସନୀୟତା: ${confidence}। ପରବର୍ତ୍ତୀ ପଦକ୍ଷେପ: ${firstAction}।`;
        } else {
            speechText = `AgriIntel diagnosis report. Detected Crop: ${crop}. Condition: ${condition}. Model confidence: ${confidence}. Recommended action: ${firstAction}. Symptoms to look for: ${firstSymptom}. Remember, confirm with an agricultural expert before treating.`;
        }

        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(speechText);
        
        // Language locale codes
        const langCodes = { en: "en-IN", hi: "hi-IN", or: "or-IN" };
        utterance.lang = langCodes[currentLanguage] || "en-IN";
        utterance.rate = 0.92;
        utterance.pitch = 1.0;

        utterance.onstart = () => {
            isSpeaking = true;
            DOM.speakBtnText.textContent = I18N[currentLanguage].stopAudio;
        };

        utterance.onend = utterance.onerror = () => {
            isSpeaking = false;
            DOM.speakBtnText.textContent = I18N[currentLanguage].listen;
        };

        window.speechSynthesis.speak(utterance);
    });
}

// =============================================================================
// KNOWLEDGE BASE (54 CROP DISEASE CLASSES)
// =============================================================================

// =============================================================================
// KNOWLEDGE BASE (108 VERIFIED CROP DISEASE PROFILES ACROSS 30 CROPS)
// =============================================================================

async function initKnowledgeBase() {
    try {
        const response = await fetch(API.CLASSES);
        if (!response.ok) throw new Error("Could not load classes catalog");
        const data = await response.json();
        
        classesCatalog = [];
        
        if (data.knowledge_catalog && data.knowledge_catalog.length > 0) {
            classesCatalog = data.knowledge_catalog.map(item => ({
                crop: item.crop,
                cropDisplay: item.crop_display || item.crop,
                className: item.class_name,
                condition: item.condition,
                conditionDisplay: item.condition_display || item.condition,
                pathogen: item.pathogen || "Not specified",
                isHealthy: Boolean(item.is_healthy),
                isVisionTrained: Boolean(item.is_vision_trained_v4),
                severity: item.severity || (item.is_healthy ? "None" : "Moderate"),
                description: item.description || "",
                symptoms: item.symptoms || [],
                recommendedNextSteps: item.recommended_next_steps || [],
                preventivePractices: item.preventive_practices || []
            }));
        } else {
            // Fallback to legacy crops structure
            const cropsObj = data.crops || {};
            for (const [cropName, classesList] of Object.entries(cropsObj)) {
                classesList.forEach(item => {
                    classesCatalog.push({
                        crop: cropName,
                        cropDisplay: cropName.replace("_", " "),
                        className: item.class_name,
                        condition: item.condition,
                        conditionDisplay: item.condition_display,
                        pathogen: "Not specified",
                        isHealthy: item.condition.toLowerCase().includes("healthy"),
                        isVisionTrained: true,
                        severity: "Moderate",
                        description: `Benchmark model class for ${cropName}.`,
                        symptoms: [],
                        recommendedNextSteps: [],
                        preventivePractices: []
                    });
                });
            }
        }

        renderCatalogGrid(classesCatalog);
        buildDynamicCatalogChips(classesCatalog);
        initCatalogFilters();

    } catch (err) {
        console.error("Knowledge base load error:", err);
        if (DOM.catalogGrid) {
            DOM.catalogGrid.innerHTML = `
                <div class="card" style="grid-column: 1/-1; text-align: center; padding: 2.5rem;">
                    <p style="color: var(--danger); font-weight: 700;">Unable to load disease knowledge catalog.</p>
                    <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 0.5rem;">Please verify that the AgriIntel Flask server is running on http://127.0.0.1:5000.</p>
                </div>
            `;
        }
    }
}

function buildDynamicCatalogChips(items) {
    if (!DOM.catalogCropChips) return;
    
    // Calculate counts per crop
    const cropCounts = {};
    items.forEach(it => {
        const c = it.cropDisplay || it.crop;
        cropCounts[c] = (cropCounts[c] || 0) + 1;
    });

    const sortedCrops = Object.keys(cropCounts).sort();

    let html = `<button type="button" class="crop-chip active" data-crop="all">All Crops (${items.length})</button>`;
    html += `<button type="button" class="crop-chip" data-crop="vision-only">Vision AI Active (54)</button>`;
    html += `<button type="button" class="crop-chip" data-crop="knowledge-only">Knowledge & Search (${items.length - 54})</button>`;

    sortedCrops.forEach(cropName => {
        html += `<button type="button" class="crop-chip" data-crop="${cropName}">${cropName} (${cropCounts[cropName]})</button>`;
    });

    DOM.catalogCropChips.innerHTML = html;
}

function renderCatalogGrid(items) {
    if (!DOM.catalogGrid) return;
    DOM.catalogGrid.innerHTML = "";

    if (items.length === 0) {
        DOM.catalogGrid.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 3rem;">
                <p class="sources-empty-state">No matching crop disease profiles found in the library.</p>
            </div>
        `;
        return;
    }

    items.forEach(item => {
        const card = document.createElement("div");
        card.className = "catalog-card";

        const badgeClass = item.isVisionTrained ? "status-trained" : "status-knowledge";
        const badgeLabel = item.isVisionTrained ? "Vision Model Active" : "Knowledge & Live Search";

        let symptomsHtml = "";
        if (item.symptoms && item.symptoms.length > 0) {
            symptomsHtml = `
                <div class="catalog-details-section">
                    <h6>Diagnostic Symptoms</h6>
                    <ul>
                        ${item.symptoms.slice(0, 3).map(s => `<li>${s}</li>`).join("")}
                    </ul>
                </div>
            `;
        }

        let preventionHtml = "";
        if (item.preventivePractices && item.preventivePractices.length > 0) {
            preventionHtml = `
                <div class="catalog-details-section">
                    <h6>Prevention & Management</h6>
                    <ul>
                        ${item.preventivePractices.slice(0, 2).map(p => `<li>${p}</li>`).join("")}
                    </ul>
                </div>
            `;
        }

        card.innerHTML = `
            <div class="catalog-card-header">
                <span class="catalog-crop-pill">🌱 ${item.cropDisplay || item.crop}</span>
                <span class="catalog-model-badge ${badgeClass}">${badgeLabel}</span>
            </div>
            <h4 class="catalog-card-title">${item.conditionDisplay}</h4>
            <p class="catalog-pathogen"><strong>Pathogen:</strong> ${item.pathogen}</p>
            <p class="catalog-desc">${item.description ? item.description.slice(0, 160) + (item.description.length > 160 ? "..." : "") : "Diagnostic profile with verified botanical guidance."}</p>
            
            <button type="button" class="catalog-expand-btn">View Symptoms & Prevention ↓</button>
            <div class="catalog-details-accordion">
                ${symptomsHtml}
                ${preventionHtml}
                <div class="catalog-card-actions">
                    <button type="button" class="btn btn-outline btn-sm" onclick="exploreAgriculturalIntel('${item.cropDisplay || item.crop}', '${item.conditionDisplay}')">
                        🔍 Research via SerpApi
                    </button>
                    ${item.isVisionTrained ? `
                        <button type="button" class="btn btn-primary btn-sm" onclick="testInStudio('${item.crop}')">
                            Test in Studio
                        </button>
                    ` : ''}
                </div>
            </div>
        `;

        const expandBtn = card.querySelector(".catalog-expand-btn");
        const accordion = card.querySelector(".catalog-details-accordion");
        expandBtn.addEventListener("click", () => {
            const isOpen = accordion.classList.contains("open");
            if (isOpen) {
                accordion.classList.remove("open");
                expandBtn.textContent = "View Symptoms & Prevention ↓";
            } else {
                accordion.classList.add("open");
                expandBtn.textContent = "Hide Details ↑";
            }
        });

        DOM.catalogGrid.appendChild(card);
    });
}

function initCatalogFilters() {
    // Search input
    if (DOM.catalogSearchInput) {
        DOM.catalogSearchInput.addEventListener("input", (e) => {
            const query = e.target.value.toLowerCase().trim();
            filterCatalog(query, getActiveCropFilter());
        });
    }

    // Crop filter chips
    if (DOM.catalogCropChips) {
        DOM.catalogCropChips.addEventListener("click", (e) => {
            const chip = e.target.closest(".crop-chip");
            if (!chip) return;

            const chips = DOM.catalogCropChips.querySelectorAll(".crop-chip");
            chips.forEach(c => c.classList.remove("active"));
            chip.classList.add("active");
            
            const selectedCrop = chip.getAttribute("data-crop");
            const query = DOM.catalogSearchInput ? DOM.catalogSearchInput.value.toLowerCase().trim() : "";
            filterCatalog(query, selectedCrop);
        });
    }
}

function getActiveCropFilter() {
    const active = DOM.catalogCropChips?.querySelector(".crop-chip.active");
    return active ? active.getAttribute("data-crop") : "all";
}

function filterCatalog(query, cropFilter) {
    let filtered = classesCatalog;

    // Filter by crop or model category
    if (cropFilter && cropFilter !== "all") {
        if (cropFilter === "vision-only") {
            filtered = filtered.filter(item => item.isVisionTrained);
        } else if (cropFilter === "knowledge-only") {
            filtered = filtered.filter(item => !item.isVisionTrained);
        } else {
            filtered = filtered.filter(item => {
                const c = (item.cropDisplay || item.crop).toLowerCase();
                return c === cropFilter.toLowerCase() || c.includes(cropFilter.toLowerCase());
            });
        }
    }

    // Filter by search query
    if (query) {
        filtered = filtered.filter(item => {
            return (item.cropDisplay || item.crop).toLowerCase().includes(query) ||
                   item.conditionDisplay.toLowerCase().includes(query) ||
                   item.className.toLowerCase().includes(query) ||
                   item.pathogen.toLowerCase().includes(query) ||
                   (item.description && item.description.toLowerCase().includes(query));
        });
    }

    renderCatalogGrid(filtered);
}

// Global hook to test crop in diagnosis studio from library
window.testInStudio = function(cropName) {
    if (DOM.cropHintSelect) {
        DOM.cropHintSelect.value = cropName;
    }
    document.getElementById("diagnosisSection")?.scrollIntoView({ behavior: "smooth" });
};

// Global hook to jump from catalog card directly into SerpApi Research Explorer
window.exploreAgriculturalIntel = function(crop, disease) {
    if (DOM.intelCropInput) DOM.intelCropInput.value = crop;
    if (DOM.intelDiseaseInput) DOM.intelDiseaseInput.value = disease;
    if (DOM.intelCategorySelect) DOM.intelCategorySelect.value = "all";
    
    const intelSec = document.getElementById("intelSection");
    if (intelSec) {
        intelSec.scrollIntoView({ behavior: "smooth" });
        // Automatically trigger search
        setTimeout(() => {
            if (DOM.intelSearchForm) {
                DOM.intelSearchForm.dispatchEvent(new Event("submit", { cancelable: true }));
            }
        }, 600);
    }
};

// =============================================================================
// AGRICULTURAL INTELLIGENCE (SERPAPI ADVANCED SEARCH)
// =============================================================================

function initIntelSearch() {
    if (!DOM.intelSearchForm) return;

    DOM.intelSearchForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const crop = DOM.intelCropInput?.value.trim() || "";
        const disease = DOM.intelDiseaseInput?.value.trim() || "";
        const category = DOM.intelCategorySelect?.value || "all";
        const query = DOM.intelCustomQuery?.value.trim() || "";

        DOM.intelSubmitBtn.disabled = true;
        DOM.intelSubmitBtn.textContent = "Searching Sources...";
        DOM.intelStatusCount.textContent = "Querying SerpApi agricultural index...";

        try {
            const response = await fetch(API.SEARCH, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ crop, disease, category, query })
            });

            const data = await response.json();
            renderIntelResults(data.sources || [], data.query_used);

            if (data.success && data.sources?.length) {
                DOM.intelStatusCount.textContent = `Found ${data.sources.length} authoritative agricultural extension sources for query: "${data.query_used}"`;
            } else {
                DOM.intelStatusCount.textContent = data.message || "No results found.";
            }

        } catch (err) {
            console.error("Intel search error:", err);
            DOM.intelStatusCount.textContent = "Error communicating with agricultural search service.";
        } finally {
            DOM.intelSubmitBtn.disabled = false;
            DOM.intelSubmitBtn.textContent = "🔍 Search Agricultural Intelligence";
        }
    });
}

function renderIntelResults(sources, queryUsed) {
    if (!DOM.intelResultsGrid) return;
    DOM.intelResultsGrid.innerHTML = "";

    if (!sources || sources.length === 0) {
        DOM.intelResultsGrid.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; padding: 2rem;">
                <p class="sources-empty-state">No matching agricultural sources found for this query. Try adjusting terms.</p>
            </div>
        `;
        return;
    }

    sources.forEach(src => {
        const item = document.createElement("article");
        item.className = "source-item";
        item.innerHTML = `
            <div class="source-badge-row">
                <span class="source-trust-badge">${src.trust_badge || "Agricultural Publication"}</span>
                <span class="source-domain-pill">🌐 ${src.domain}</span>
            </div>
            <h4 class="source-title">${escapeHtml(src.title)}</h4>
            <p class="source-snippet">${escapeHtml(src.snippet)}</p>
            <a href="${src.link}" target="_blank" rel="noopener noreferrer" class="source-link">
                View Official Publication ↗
            </a>
        `;
        DOM.intelResultsGrid.appendChild(item);
    });
}

// =============================================================================
// LANGUAGE SWITCHER
// =============================================================================

function initLanguageSwitcher() {
    if (!DOM.langSelect) return;

    DOM.langSelect.addEventListener("change", (e) => {
        currentLanguage = e.target.value;
        applyLanguage(currentLanguage);
    });
}

function applyLanguage(lang) {
    const texts = I18N[lang] || I18N.en;

    // Apply translations
    const heroTitle = document.getElementById("heroTitle");
    const heroSubtitle = document.getElementById("heroSubtitle");
    const heroBadgeText = document.getElementById("heroBadgeText");
    const startDiagnosisBtn = document.getElementById("startDiagnosisBtn");
    const exploreLibraryBtn = document.getElementById("exploreLibraryBtn");
    const dropzonePrompt = document.getElementById("dropzonePrompt");
    const dropzoneSubtext = document.getElementById("dropzoneSubtext");
    const browseFileBtn = document.getElementById("browseFileBtn");
    const cameraSnapBtn = document.getElementById("cameraSnapBtn");

    if (heroTitle) {
        heroTitle.innerHTML = `${texts.heroTitle} <span class="text-gradient">${texts.heroTitleHighlight}</span>`;
    }
    if (heroSubtitle) heroSubtitle.textContent = texts.heroSubtitle;
    if (heroBadgeText) heroBadgeText.textContent = texts.heroBadge;
    if (startDiagnosisBtn) startDiagnosisBtn.textContent = texts.startDiagnosis;
    if (exploreLibraryBtn) exploreLibraryBtn.textContent = texts.exploreLibrary;
    if (dropzonePrompt) dropzonePrompt.textContent = texts.dropzonePrompt;
    if (dropzoneSubtext) dropzoneSubtext.textContent = texts.dropzoneSubtext;
    if (browseFileBtn) browseFileBtn.textContent = texts.choosePhoto;
    if (cameraSnapBtn) cameraSnapBtn.textContent = texts.useCamera;
    if (DOM.analyzeImageBtn && !selectedFile) DOM.analyzeImageBtn.textContent = texts.analyzeLeaf;
    if (DOM.speakBtnText) DOM.speakBtnText.textContent = texts.listen;
}

// =============================================================================
// UTILITIES
// =============================================================================

function escapeHtml(str) {
    if (!str) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
