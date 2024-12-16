import matplotlib.pyplot as plt

# Create a sequence diagram using matplotlib
fig, ax = plt.subplots(figsize=(12, 6))

# Set diagram limits and labels
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Draw vertical lifelines
services = [
    "Client",
    "File Upload API",
    "Apache Kafka",
    "Extract Text API",
    "Embeddings API",
    "Summarize Text API",
    "Temporal Orchestrator"
]

x_positions = [1, 2.5, 4, 5.5, 7, 8.5, 10]
y_start = 9
y_end = 1

for x in x_positions:
    ax.plot([x, x], [y_start, y_end], linestyle="--", color="gray")
for i, service in enumerate(services):
    ax.text(x_positions[i], y_start + 0.5, service, ha="center", fontsize=10, fontweight="bold")

# Draw interactions
interactions = [
    ("Client", "File Upload API", "Upload File"),
    ("File Upload API", "Apache Kafka", "Publish 'file_uploaded'"),
    ("Apache Kafka", "Extract Text API", "Consume 'file_uploaded'"),
    ("Extract Text API", "Apache Kafka", "Publish 'text_extracted'"),
    ("Apache Kafka", "Embeddings API", "Consume 'text_extracted'"),
    ("Embeddings API", "Apache Kafka", "Publish 'embeddings_generated'"),
    ("Apache Kafka", "Summarize Text API", "Consume 'embeddings_generated'"),
    ("Summarize Text API", "Apache Kafka", "Publish 'summary_generated'"),
    ("Apache Kafka", "Temporal Orchestrator", "Consume 'summary_generated'"),
    ("Temporal Orchestrator", "Client", "Return Workflow Result")
]

y_pos = y_start - 0.5
arrow_props = dict(arrowstyle="->", color="blue", lw=1.5)

for interaction in interactions:
    src, dst, label = interaction
    src_x = x_positions[services.index(src)]
    dst_x = x_positions[services.index(dst)]
    ax.annotate(
        label,
        xy=(dst_x, y_pos),
        xytext=(src_x, y_pos),
        arrowprops=arrow_props,
        fontsize=9,
        ha="center"
    )
    y_pos -= 0.8

# Save and show the diagram
plt.tight_layout()
plt.savefig("event_driven_workflow_sequence_diagram.png", dpi=300)
plt.show()
