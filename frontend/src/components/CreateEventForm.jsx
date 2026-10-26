import { useState } from 'react';

export default function CreateEventForm({ onEventCreated }) {
  const [isOpen, setIsOpen] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    scheduled_start: '',
  });
  const [errors, setErrors] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [apiError, setApiError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: null }));
    }
  };

  const validate = () => {
    const errs = {};
    if (!formData.title.trim()) {
      errs.title = 'Event title is required.';
    }
    if (!formData.scheduled_start) {
      errs.scheduled_start = 'Scheduled date & time is required.';
    }
    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setApiError(null);
    if (!validate()) return;

    setSubmitting(true);
    try {
      // Convert datetime-local to ISO string
      const isoDate = new Date(formData.scheduled_start).toISOString();
      await onEventCreated({
        title: formData.title.trim(),
        description: formData.description.trim() || undefined,
        scheduled_start: isoDate,
      });

      // Reset form and collapse
      setFormData({
        title: '',
        description: '',
        scheduled_start: '',
      });
      setIsOpen(false);
    } catch (err) {
      setApiError(err.message || 'Failed to create event.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className={`create-event-wrapper ${isOpen ? 'open' : ''}`}>
      <div className="create-event-header" onClick={() => setIsOpen(!isOpen)}>
        <div>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--ink)' }}>
            {isOpen ? 'New Event Details' : 'Host a New Event'}
          </h3>
          <p style={{ fontSize: '0.85rem', color: 'var(--slate)' }}>
            Schedule and broadcast a live meeting to your community
          </p>
        </div>

        <button
          type="button"
          className="btn btn-primary"
          style={{ padding: '8px 16px', fontSize: '0.9rem' }}
          onClick={(e) => {
            e.stopPropagation();
            setIsOpen(!isOpen);
          }}
        >
          {isOpen ? 'Close' : '+ Create Event'}
        </button>
      </div>

      {isOpen && (
        <form className="create-event-body" onSubmit={handleSubmit}>
          {apiError && <div className="alert alert-error">{apiError}</div>}

          <div className="form-group">
            <label className="form-label" htmlFor="title">
              Event Title *
            </label>
            <input
              id="title"
              name="title"
              type="text"
              className={`form-input ${errors.title ? 'has-error' : ''}`}
              placeholder="e.g. Community Tech Sync"
              value={formData.title}
              onChange={handleChange}
            />
            {errors.title && <span className="field-error">{errors.title}</span>}
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="description">
              Description (Optional)
            </label>
            <textarea
              id="description"
              name="description"
              rows={3}
              className="form-textarea"
              placeholder="Outline the agenda or speakers for this session..."
              value={formData.description}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="scheduled_start">
              Scheduled Date & Time *
            </label>
            <input
              id="scheduled_start"
              name="scheduled_start"
              type="datetime-local"
              className={`form-input ${errors.scheduled_start ? 'has-error' : ''}`}
              value={formData.scheduled_start}
              onChange={handleChange}
            />
            {errors.scheduled_start && (
              <span className="field-error">{errors.scheduled_start}</span>
            )}
          </div>

          <div style={{ display: 'flex', gap: '12px', justifyContent: 'flex-end', marginTop: '16px' }}>
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => setIsOpen(false)}
              disabled={submitting}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn btn-primary"
              disabled={submitting}
            >
              {submitting ? 'Creating Event...' : 'Publish Event'}
            </button>
          </div>
        </form>
      )}
    </div>
  );
}
